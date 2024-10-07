import financedatabase as fd
import json
import streamlit as st


class tran:
    def __init__(self, file_path):
        self.tran = self.load_file(file_path)

    def load_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            tran = json.load(f)
        return tran

    def tran_country(self, country):
        return self.tran.get(country, country)

    def tran_industry(self, industry):
        return self.tran.get(industry, industry)

    def tarn_marketcap(self, marketcap):
        return self.tran.get(marketcap, marketcap)

    def tran_currency(self, currency):
        return self.tran.get(currency, currency)

    def tran_category(self, category):
        return self.tran.get(category, category)

    def tran_market(self, market):
        return self.tran.get(market, market)

    def tran_category_fund(self, category_fund):
        return self.tran.get(category_fund, category_fund)


class Equities:
    @st.cache_data
    def search(_self, country, currency, industry, marketcap):
        equities = fd.Equities()
        result = equities.search(
            country=country, currency=currency, industry=industry, market_cap=marketcap
        )
        return result


class ETFs:
    @st.cache_data
    def search(_self, category, market, currency):
        etfs = fd.ETFs()
        result = etfs.search(category=category, market=market, currency=currency)
        return result


class Funds:
    @st.cache_data
    def search(_self, category, market, currency):
        funds = fd.Funds()
        result = funds.search(category=category, market=market, currency=currency)
        return result


def app():
    st.set_page_config(page_title="MarketSearch", layout="wide", page_icon="📈")

    # 隱藏footer
    hide_menu_style = "<style> footer {visibility: hidden;} </style>"
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    # 標題及樣式
    st.markdown(
        "<h1 style='text-align: center; color: rainbow;'>📈MarketSearch</h1>",
        unsafe_allow_html=True,
    )
    st.subheader(" ", divider="rainbow")
    st.sidebar.title("📊 Menu")

    # 初始化翻譯字典
    country_obj = tran("country.json")
    currency_obj = tran("currency.json")
    industry_obj = tran("industry.json")
    marketcap_obj = tran("marketcap.json")
    category_obj = tran("category.json")
    market_obj = tran("market.json")
    category_fund_obj = tran("category_fund.json")

    options = st.sidebar.selectbox("選擇功能", ["股票搜尋", "ETF搜尋", "基金搜尋"])
    st.sidebar.markdown(
        """
    免責聲明：        
    1. 本平台僅適用於數據搜尋，不建議任何投資行為
    2. 排版問題建議使用電腦查詢數據  
    3. 其他專案：[MarketInfo](https://market-info-usa.streamlit.app)  
    """
    )

    if options == "股票搜尋":
        countries = [
            "Afghanistan",
            "Anguilla",
            "Argentina",
            "Australia",
            "Austria",
            "Azerbaijan",
            "Bahamas",
            "Bangladesh",
            "Barbados",
            "Belgium",
            "Belize",
            "Bermuda",
            "Botswana",
            "Brazil",
            "British Virgin Islands",
            "Cambodia",
            "Canada",
            "Cayman Islands",
            "Chile",
            "China",
            "Colombia",
            "Costa Rica",
            "Cyprus",
            "Czech Republic",
            "Denmark",
            "Dominican Republic",
            "Egypt",
            "Estonia",
            "Falkland Islands",
            "Finland",
            "France",
            "French Guiana",
            "Gabon",
            "Georgia",
            "Germany",
            "Ghana",
            "Gibraltar",
            "Greece",
            "Greenland",
            "Guernsey",
            "Hong Kong",
            "Hungary",
            "Iceland",
            "India",
            "Indonesia",
            "Ireland",
            "Isle of Man",
            "Israel",
            "Italy",
            "Ivory Coast",
            "Japan",
            "Jersey",
            "Jordan",
            "Kazakhstan",
            "Kenya",
            "Kyrgyzstan",
            "Latvia",
            "Liechtenstein",
            "Lithuania",
            "Luxembourg",
            "Macau",
            "Macedonia",
            "Malaysia",
            "Malta",
            "Mauritius",
            "Mexico",
            "Monaco",
            "Mongolia",
            "Montenegro",
            "Morocco",
            "Mozambique",
            "Myanmar",
            "Namibia",
            "Netherlands",
            "Netherlands Antilles",
            "New Zealand",
            "Nigeria",
            "Norway",
            "Panama",
            "Papua New Guinea",
            "Peru",
            "Philippines",
            "Poland",
            "Portugal",
            "Qatar",
            "Reunion",
            "Romania",
            "Russia",
            "Saudi Arabia",
            "Senegal",
            "Singapore",
            "Slovakia",
            "Slovenia",
            "South Africa",
            "South Korea",
            "Spain",
            "Suriname",
            "Sweden",
            "Switzerland",
            "Taiwan",
            "Tanzania",
            "Thailand",
            "Turkey",
            "Ukraine",
            "United Arab Emirates",
            "United Kingdom",
            "United States",
            "Uruguay",
            "Vietnam",
            "Zambia",
        ]
        industries = [
            "Aerospace & Defense",
            "Air Freight & Logistics",
            "Airlines",
            "Auto Components",
            "Automobiles",
            "Banks",
            "Beverages",
            "Biotechnology",
            "Building Products",
            "Capitalindustrys",
            "Chemicals",
            "Commercial Services & Supplies",
            "Communications Equipment",
            "Construction & Engineering",
            "Construction Materials",
            "Consumer Finance",
            "Distributors",
            "Diversified Consumer Services",
            "Diversified Financial Services",
            "Diversified Telecommunication Services",
            "Electric Utilities",
            "Electrical Equipment",
            "Electronic Equipment, Instruments & Components",
            "Energy Equipment & Services",
            "Entertainment",
            "Equity Real Estate Investment Trusts (REITs)",
            "Food & Staples Retailing",
            "Food Products",
            "Gas Utilities",
            "Health Care Equipment & Supplies",
            "Health Care Providers & Services",
            "Health Care Technology",
            "Hotels, Restaurants & Leisure",
            "Household Durables",
            "Household Products",
            "IT Services",
            "Independent Power and Renewable Electricity Producers",
            "Industrial Conglomerates",
            "Insurance",
            "Interactive Media & Services",
            "Internet & Directindustrying Retail",
            "Machinery",
            "Marine",
            "Media",
            "Metals & Mining",
            "Multi-Utilities",
            "Oil, Gas & Consumable Fuels",
            "Paper & Forest Products",
            "Pharmaceuticals",
            "Professional Services",
            "Real Estate Management & Development",
            "Road & Rail",
            "Semiconductors & Semiconductor Equipment",
            "Software",
            "Specialty Retail",
            "Technology Hardware, Storage & Peripherals",
            "Textiles, Apparel & Luxury Goods",
            "Thrifts & Mortgage Finance",
            "Tobacco",
            "Trading Companies & Distributors",
            "Transportation Infrastructure",
            "Water Utilities",
        ]
        marketcaps = [
            "Large Cap",
            "Mega Cap",
            "Micro Cap",
            "Mid Cap",
            "Nano Cap",
            "Small Cap",
        ]
        currencies = [
            "ARS",
            "AUD",
            "BRL",
            "CAD",
            "CHF",
            "CLP",
            "CNY",
            "COP",
            "CZK",
            "DKK",
            "EUR",
            "GBP",
            "HKD",
            "HUF",
            "IDR",
            "ILA",
            "ILS",
            "INR",
            "ISK",
            "JPY",
            "KES",
            "KRW",
            "LKR",
            "MXN",
            "MYR",
            "NOK",
            "NZD",
            "PEN",
            "PHP",
            "PLN",
            "QAR",
            "RUB",
            "SAR",
            "SEK",
            "SGD",
            "THB",
            "TRY",
            "TWD",
            "USD",
            "ZAR",
            "ZAc",
        ]
        # 翻譯國家、產業和市值名稱
        tran_country = [country_obj.tran_country(c) for c in countries]
        tran_industry = [industry_obj.tran_industry(i) for i in industries]
        tarn_marketcap = [marketcap_obj.tarn_marketcap(m) for m in marketcaps]
        tran_currency = [currency_obj.tran_currency(e) for e in currencies]

        country = st.selectbox("選擇國家", tran_country)
        industry = st.selectbox("選擇產業", tran_industry)
        marketcap = st.selectbox("選擇市值", tarn_marketcap)
        currency = st.selectbox("選擇貨幣", tran_currency)

        if st.button("搜尋"):
            equity_obj = Equities()
            # 將翻譯過的國家、產業、市值範疇轉回原始名稱進行查詢
            country = countries[tran_country.index(country)]
            currency = currencies[tran_currency.index(currency)]
            industry = industries[tran_industry.index(industry)]
            marketcap = marketcaps[tarn_marketcap.index(marketcap)]

            result = equity_obj.search(country, currency, industry, marketcap)
            if not result.empty:
                st.dataframe(result)
            else:
                st.error("查無搜尋結果")

    elif options == "ETF搜尋":
        # category, market, currency
        categories = [
            "Alternative",
            "Bonds",
            "Commodities Broad Basket",
            "Communications",
            "Consumer Discretionary",
            "Consumer Staples",
            "Currencies",
            "Derivatives",
            "Developed Markets",
            "Emerging Markets",
            "Energy",
            "Equities",
            "Factors",
            "Financials",
            "Health Care",
            "Industrials",
            "Materials",
            "Real Estate",
            "Technology",
            "Trading",
            "Utilities",
        ]
        markets = [
            "at_market",
            "au_market",
            "be_market",
            "ca_market",
            "ch_market",
            "cz_market",
            "de_market",
            "dk_market",
            "dr_market",
            "es_market",
            "fi_market",
            "fr_market",
            "gb_market",
            "gr_market",
            "hu_market",
            "ic_market",
            "ie_market",
            "il_market",
            "it_market",
            "jp_market",
            "kr_market",
            "mx_market",
            "nl_market",
            "no_market",
            "pt_market",
            "qa_market",
            "ru_market",
            "se_market",
            "sg_market",
            "sr_market",
            "th_market",
            "tr_market",
            "tw_market",
            "us_market",
            "vs_market",
        ]
        currencies = [
            "AUD",
            "CAD",
            "CHF",
            "CNY",
            "CZK",
            "DKK",
            "EUR",
            "GBP",
            "HUF",
            "ILA",
            "ISK",
            "JPY",
            "KRW",
            "MXN",
            "NOK",
            "QAR",
            "RUB",
            "SAR",
            "SEK",
            "SGD",
            "THB",
            "TRY",
            "TWD",
            "USD",
        ]

        tran_category = [category_obj.tran_category(c) for c in categories]
        tran_market = [market_obj.tran_market(m) for m in markets]
        tran_currency = [currency_obj.tran_currency(e) for e in currencies]

        category = st.selectbox("選擇類別", tran_category)
        market = st.selectbox("選擇市場", tran_market)
        currency = st.selectbox("選擇貨幣", tran_currency)

        if st.button("搜尋"):
            etf_obj = ETFs()
            category = categories[tran_category.index(category)]
            market = markets[tran_market.index(market)]
            currency = currencies[tran_currency.index(currency)]

            result = etf_obj.search(category, market, currency)
            if not result.empty:
                st.dataframe(result)
            else:
                st.error("查無搜尋結果")

    elif options == "基金搜尋":
        # category, market, currency
        category_funds = [
            "Africa",
            "Allocation",
            "Alternative",
            "Asia",
            "Australia",
            "Austria",
            "Bonds",
            "Canada",
            "China",
            "Commodities",
            "Communications",
            "Consumer Discretionary",
            "Consumer Staples",
            "Debt",
            "Derivatives",
            "Emerging Markets",
            "Energy",
            "Equities",
            "Europe",
            "Factors",
            "Financials",
            "France",
            "Germany",
            "Health Care",
            "Hong Kong",
            "India",
            "Industrials",
            "Infrastructure",
            "Islamic",
            "Italy",
            "Japan",
            "Latin America",
            "Loans",
            "Mexico",
            "Miscellaneous",
            "Netherlands",
            "New Zealand",
            "North America",
            "Real Estate",
            "Scandinavia",
            "Sector",
            "Spain",
            "Target Date",
            "Technology",
            "Thailand",
            "Trading",
            "United Kingdom",
            "United States",
            "Utilities",
            "Vietnam",
            "World",
        ]
        markets = [
            "at_market",
            "ca_market",
            "ch_market",
            "cn_market",
            "dr_market",
            "es_market",
            "fr_market",
            "gb_market",
            "hk_market",
            "hu_market",
            "id_market",
            "ie_market",
            "il_market",
            "in_market",
            "it_market",
            "jp_market",
            "kr_market",
            "mx_market",
            "nl_market",
            "nz_market",
            "pt_market",
            "ru_market",
            "se_market",
            "sg_market",
            "sr_market",
            "tw_market",
            "us24_market",
            "us_market",
        ]
        currencies = [
            "AUD",
            "CAD",
            "CHF",
            "CNH",
            "CNY",
            "CZK",
            "EUR",
            "GBP",
            "HKD",
            "HUF",
            "IDR",
            "ILS",
            "INR",
            "JPY",
            "KRW",
            "MXN",
            "NOK",
            "NZD",
            "PLN",
            "RUB",
            "SAR",
            "SEK",
            "SGD",
            "TWD",
            "USD",
        ]

        tran_category_fund = [category_fund_obj.tran_category_fund(c) for c in category_funds]
        tran_market = [market_obj.tran_market(m) for m in markets]
        tran_currency = [currency_obj.tran_currency(e) for e in currencies]

        category_fund = st.selectbox("選擇類別", tran_category_fund)
        market = st.selectbox("選擇市場", tran_market)
        currency = st.selectbox("選擇貨幣", tran_currency)

        if st.button("搜尋"):
            fund_obj = Funds()
            category = category_funds[tran_category_fund.index(category_fund)]
            market = markets[tran_market.index(market)]
            currency = currencies[tran_currency.index(currency)]

            result = fund_obj.search(category, market, currency)
            if not result.empty:
                st.dataframe(result)
            else:
                st.error("查無搜尋結果")


if __name__ == "__main__":
    app()
