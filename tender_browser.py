# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "beautifulsoup4==4.13.5",
#     "ollama==0.5.4",
#     "pandas==2.3.2",
#     "requests==2.32.5",
#     "selenium==4.35.0",
# ]
# ///

import marimo

__generated_with = "0.16.3"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from bs4 import BeautifulSoup
    from io import StringIO
    from datetime import datetime

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import WebDriverException

    import ollama
    return (
        BeautifulSoup,
        By,
        EC,
        Options,
        StringIO,
        WebDriverException,
        WebDriverWait,
        datetime,
        mo,
        ollama,
        pd,
        webdriver,
    )


@app.cell
def _(mo):
    mo.md(
        """
    # 📋 Tender Browser & AI Assistant

    Navigate to the [Biuletyn Zamówień Publicznych](https://ezamowienia.gov.pl/mo-client-board/bzp/list) website to download CSV file with tender data. You can also filter offers on this website.

    Upload a CSV file with tender data, view all tenders at once, 
    select one for detailed analysis, and chat with an AI assistant about it.
    """
    )
    return


@app.cell
def _(mo):
    file_upload = mo.ui.file(
        label="Upload CSV file with tender data",
        multiple=False,
    )
    file_upload
    return (file_upload,)


@app.cell
def _(StringIO, file_upload, mo, pd):
    # Load and validate CSV data
    if not file_upload.name():
        tenders_df = None
        mo.stop(True, mo.md("Please upload a CSV file to continue."))
    else:
        csv_content = file_upload.contents().decode("utf-8")
        tenders_df = pd.read_csv(StringIO(csv_content), sep=";")
    return (tenders_df,)


@app.cell
def _(mo, tenders_df):
    mo.md(
        f"""**Total tenders:** {len(tenders_df) if tenders_df is not None else 0}"""
    )
    return


@app.cell
def _(mo, tenders_df):
    # Display all tenders
    if tenders_df is not None:
        # Display as interactive table
        tender_table = mo.ui.table(tenders_df, selection="single")

        mo.vstack(
            [mo.md(f"### All Tenders ({len(tenders_df)} total)"), tender_table]
        )
    else:
        tender_table = None
        all_tenders = None
    return (tender_table,)


@app.cell
def _(tender_table):
    tender_table
    return


@app.cell
def _(mo, tender_table, tenders_df):
    # Tender selection and confirmation
    display_content = None

    if tender_table is not None and tenders_df is not None:
        # Use run_button for triggering computation
        analyze_button = mo.ui.run_button(label="🔍 Analyze Selected Tender")

        if tender_table.value is not None and len(tender_table.value) > 0:
            # tender_table.value contains the selected rows as a DataFrame
            selected_tender = tender_table.value.iloc[
                0
            ]  # Get the first (and only) selected row

            display_content = mo.vstack(
                [
                    mo.md("### Selected Tender Preview:"),
                    mo.md(f"**Name:** {selected_tender['Nazwa zamówienia']}"),
                    mo.md(f"**Issuer:** {selected_tender['Nazwa zamawiającego']}"),
                    analyze_button,
                ]
            )
        else:
            selected_tender = None
            display_content = mo.md(
                "👆 Please select a tender from the table above"
            )
    else:
        analyze_button = None
        selected_tender = None
        mo.md("No tenders available")
    return analyze_button, display_content, selected_tender


@app.cell
def _(display_content):
    display_content
    return


@app.cell
def _(By, EC, Options, WebDriverWait, webdriver):
    "Functions that help to scrappe content"


    def init_driver():
        # Setup Chrome options for headless browsing
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )

        # Initialize Chrome driver
        # service = Service(executable_path=chromedriver_path)
        # driver = webdriver.Chrome(options=chrome_options, service=service)
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_page_load_timeout(30)

        return driver


    def wait_for_headers(driver):
        wait = WebDriverWait(driver, 15)
        h1_tags = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "h1"))
        )
        h3_tags = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "h3"))
        )
        return h1_tags, h3_tags


    def parse_bidder_qualifications(h3_tag) -> str:
        qualifications = ""
        for tag in h3_tag.next_siblings:
            if tag.name == "h3":
                break
            if tag.name == "br":
                qualifications += "\n"
            qualification = tag.get_text(strip=True)
            if qualification:
                qualifications += qualification

        return qualifications


    def scrape_patterns(h3_tags: list, patterns: dict) -> dict:
        scrapped_data = {key: None for key in patterns}
        scrapped_data["description"] = []  # store multiple parts as a list

        for h3_tag in h3_tags:
            h3_tag_text = h3_tag.get_text(strip=True)

            # Match header prefixes
            for key, prefix in patterns.items():
                if h3_tag_text.startswith(prefix + ".)"):
                    if key == "website":
                        scrapped_data[key] = h3_tag_text.split()[-1].strip()
                    elif key == "description":
                        continue
                    elif key == "bidders_qualification":
                        scrapped_data["bidders_qualification"] = (
                            parse_bidder_qualifications(h3_tag)
                        )
                    else:
                        scrapped_data[key] = h3_tag.find("span").get_text(
                            strip=True
                        )
                    break  # done with this tag

            # Tender description(s)
            if h3_tag_text.startswith(patterns["description"]):
                sibling = h3_tag.find_next_sibling()
                if sibling:
                    scrapped_data["description"].append(
                        sibling.get_text(strip=True)
                    )

        # Assemble description depending if it has parts or not
        if scrapped_data.get("tender_parts"):
            scrapped_data["description"] = "\n".join(
                f"Part {i + 1}\n {desc}"
                for i, desc in enumerate(scrapped_data["description"])
            )
        elif scrapped_data["description"] and isinstance(
            scrapped_data["description"], list
        ):
            scrapped_data["description"] = scrapped_data["description"][0]
        return scrapped_data
    return init_driver, scrape_patterns, wait_for_headers


@app.cell
def _(
    BeautifulSoup,
    WebDriverException,
    init_driver,
    scrape_patterns,
    wait_for_headers,
):
    # Enhanced web scraping functionality for dynamic content
    def scrape_tender_details_dynamic(url):
        """Scrape tender details from dynamic content using Selenium"""
        try:
            driver = init_driver()
            driver.get(url)

            h1_tags, h3_tags = wait_for_headers(driver)

            page_source = driver.page_source
            driver.quit()
            soup = BeautifulSoup(page_source, "html.parser")

            patterns = {
                "email_address": "1.5.9",
                "phone_number": "1.5.7",
                "website": "1.5.10",
                "contracting_authority_type": "1.6",
                "wadium": "6.4",
                "deadline": "8.1",
                "value": "4.1.5",
                "bidders_qualification": "5.4",
                "tender_parts": "4.1.9",
                "description": "4.2.2",
            }

            h3_tags = soup.find_all("h3", class_="mb-0")

            scrapped_data = scrape_patterns(h3_tags, patterns)

            scrapped_data["whole_text"] = soup.text

            return scrapped_data

        except WebDriverException as e:
            return {
                "error": f"WebDriver error {e}. Make sure Chrome browser is installed."
            }
    return (scrape_tender_details_dynamic,)


@app.cell
def _(analyze_button, mo, pd, scrape_tender_details_dynamic, selected_tender):
    # Trigger scraping when button is clicked
    if (
        analyze_button is not None
        and analyze_button.value
        and selected_tender is not None
    ):
        tender_url = selected_tender["Szczegóły"]
        if pd.notna(tender_url) and tender_url.strip():
            # Clear previous state and show loading message
            mo.md("🔄 **Scraping tender details with dynamic content loading...**")
            scraped_info = scrape_tender_details_dynamic(tender_url)
        else:
            scraped_info = {"error": "No valid URL found for this tender"}
    else:
        scraped_info = None
    return (scraped_info,)


@app.cell
def _(datetime, scraped_info, selected_tender):
    def get_summary_info():
        publication_date = datetime.fromisoformat(
            selected_tender["Data publikacji"].split(".")[0]
        )
        publication_date_formatted = f"{publication_date:%Y-%m-%d %H:%M}"

        summary_parts = [
            "## 📊 Tender Analysis Summary",
            "",
            f"**Tender Name:** {selected_tender['Nazwa zamówienia']}",
            "",
            f"**Issuing Organization:** {selected_tender['Nazwa zamawiającego']}",
            "",
            f"**Location:** {selected_tender['Miejscowość zamawiającego']}, {selected_tender['Województwo zamawiającego']}",
            "",
            f"**Publication Date:** {publication_date_formatted}",
            "",
        ]

        if scraped_info.get("contracting_authority_type"):
            summary_parts.append(
                f"**Type of Contracting Authority:** {scraped_info['contracting_authority_type']}"
            )
            summary_parts.append("")

        if scraped_info.get("deadline"):
            summary_parts.append(
                f"**Submission deadline:** {scraped_info['deadline']}"
            )
            summary_parts.append("")

        if scraped_info.get("value"):
            summary_parts.append(f"**Estimated Value:** {scraped_info['value']}")
            summary_parts.append("")

        summary_parts.append(f"**Contact:**")
        if scraped_info.get("phone"):
            summary_parts.append(f"Phone Number: {scraped_info['phone']}")
        if scraped_info.get("email_address"):
            summary_parts.append(f"Email Address: {scraped_info['email_address']}")
        if scraped_info.get("website"):
            summary_parts.append(f"Website: {scraped_info['website']}")
        summary_parts.append("")

        if scraped_info.get("wadium"):
            summary_parts.append(f"**Wadium:** {scraped_info['wadium']}")
            summary_parts.append("")

        if scraped_info.get("description"):
            summary_parts.append("**Description:**")
            summary_parts.append(scraped_info["description"])
            summary_parts.append("")

        if scraped_info.get("bidders_qualification"):
            summary_parts.append("**Bidders Qualification**")
            summary_parts.append(scraped_info["bidders_qualification"])
            summary_parts.append("")

        summary_parts.append(f"**Source URL:** {selected_tender['Szczegóły']}")
        return summary_parts
    return (get_summary_info,)


@app.cell
def _(get_summary_info, mo, scraped_info):
    # Generate tender summary
    if scraped_info is not None:
        if "error" in scraped_info:
            mo.md(f"❌ **Error:** {scraped_info['error']}")
            tender_summary = None
        else:
            summary_parts = get_summary_info()

            tender_summary = "\n".join(summary_parts)
    else:
        tender_summary = None
    return (tender_summary,)


@app.cell
def _(mo, tender_summary):
    mo.md(tender_summary if tender_summary is not None else "")
    return


@app.cell
def _(ollama, scraped_info, selected_tender):
    # Ollama chatbot implementation with proper ChatMessage handling
    def ollama_chat_model(messages, config):
        """Chat model using TinyLlama via Ollama."""
        if scraped_info is None or selected_tender is None:
            return "Please select and analyze a tender first."

        try:
            context = f"""
    You are an AI assistant helping to analyze a public tender.

    Tender Information:
    - Name: {selected_tender["Nazwa zamówienia"]}
    - Issuer: {selected_tender["Nazwa zamawiającego"]}
    - Location: {selected_tender["Miejscowość zamawiającego"]}
    - Publication Date: {selected_tender["Data publikacji"]}

    Scraped details:
    {[(key, value) for key, value in scraped_info.items() if key != "whole_text"]}

    Instructions:
    Answer questions about this tender based only on the provided information.
    If the question is in Polish, respond in Polish.
    """

            ollama_messages = [{"role": "system", "content": context}]
            ollama_messages.extend(
                [{"role": m.role, "content": m.content} for m in messages]
            )

            response = ollama.chat(
                model="tinyllama", messages=ollama_messages, stream=False
            )
            return response["message"]["content"]

        except Exception as e:
            return f"❌ Error communicating with Ollama: {e}\n\nMake sure Ollama is running and TinyLlama is installed:\n- ollama pull tinyllama"
    return (ollama_chat_model,)


@app.cell
def _(mo, ollama_chat_model, tender_summary):
    # Create chatbot widget
    chatbot_display = None

    if tender_summary is not None:
        chatbot = mo.ui.chat(
            ollama_chat_model,
            prompts=[
                "What is this tender about?",
                "Who is the issuing organization?",
                "What is the estimated value?",
                "When is the submission deadline?",
                "Co to za przetarg?",
                "Kto jest organizatorem?",
            ],
            show_configuration_controls=False,
        )

        chatbot_display = mo.vstack(
            [
                mo.md("## 🤖 AI Assistant"),
                mo.md("Ask questions about the selected tender:"),
                chatbot,
            ]
        )
    else:
        chatbot = None
    return (chatbot_display,)


@app.cell
def _(chatbot_display):
    chatbot_display
    return


if __name__ == "__main__":
    app.run()
