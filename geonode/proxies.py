import requests
import random
# import json


class Proxylist:
    def __init__(self, limit: int = 50, page: int = 1,
                 sort_by: str = "lastChecked", sort_type: str = "desc",
                 google_passed: int = 1,
                 anonymity_HIA: bool = True, anonymity_ANM: bool = True, anonymity_NOA: bool = True,
                 speed: int = None,
                 port: int = None,
                 p_http: bool = True, p_https: bool = True, p_socks4: bool = True, p_socks5: bool = True,
                 uptime: int = None,
                 last_checked: int = None,
                 org_and_asn: int = None,
                 country: int = None, country_code_custom: str = None
                 ):
        # Base
        self.limit = limit
        self.page = page

        # Anonymity
        self.anonymity_HIA = anonymity_HIA
        self.anonymity_ANM = anonymity_ANM
        self.anonymity_NOA = anonymity_NOA

        # Google Passed
        self.google_passed = google_passed

        # Speed
        self.speed = speed

        # Port
        self.port = port

        # Protocols
        self.p_http = p_http
        self.p_https = p_https
        self.p_socks4 = p_socks4
        self.p_socks5 = p_socks5
        if self.p_http and self.p_https:
            self.all_http = True
            self.all_socks = False
        if self.p_socks4 and self.p_socks5:
            self.all_http = False
            self.all_socks = True

        self.uptime = uptime
        self.last_checked = last_checked
        self.org_and_asn = org_and_asn
        self.country = country
        self.sort_by = sort_by
        self.sort_type = sort_type
        self.country_code_custom = country_code_custom

    def get_link(self):
        final_link = "https://proxylist.geonode.com/api/proxy-list"

        # Main
        final_link += f"?limit={self.limit}"
        final_link += f"&page={self.page}"

        # Basic Filters
        if self.sort_by.lower() != "none":
            final_link += f"&sort_by={self.sort_by}"

        if self.sort_type.lower() != "none":
            final_link += f"&sort_type={self.sort_type}"

        # Anonymity
        if self.anonymity_HIA:
            final_link += "&anonymityLevel=elite"
        elif self.anonymity_ANM:
            final_link += "&anonymityLevel=anonymous"
        elif self.anonymity_NOA:
            final_link += "&anonymityLevel=transparent"

        # Google Passed
        if self.google_passed == 1:
            pass
        elif self.google_passed == 2:
            final_link += "&google=true"
        elif self.google_passed == 3:
            final_link += "&google=false"

        # Speed
        if (self.speed == 0) or (self.speed is None):
            pass
        else:
            if self.speed == 1:
                final_link += "&speed=slow"
            elif self.speed == 2:
                final_link += "&speed=medium"
            elif self.speed == 3:
                final_link += "&speed=fast"

        # Port
        if self.port is not None:
            final_link += f"&filterPort={self.port}"

        # Protocols
        if ((self.p_http and self.p_https and self.p_socks4 and self.p_socks5) is None) or ((self.p_http and self.p_https and self.p_socks4 and self.p_socks5) == False):
            pass
        else:
            if self.all_http:
                final_link += "&protocols=http%2Chttps"
            elif self.all_socks:
                final_link += "&protocols=socks4%2Csocks5"
            elif self.all_http and self.all_socks:
                final_link += "&protocols=http%2Chttps%2Csocks4%2Csocks5"
            else:
                if self.p_http:
                    final_link += "&protocols=http"
                elif self.p_https:
                    final_link += "&protocols=https"
                elif self.p_socks4:
                    final_link += "&protocols=socks4"
                elif self.p_socks5:
                    final_link += "&protocols=socks5"

        # Country
        if self.country_code_custom is not None:
            final_link += f"&country={self.country_code_custom}"
        else:
            if self.country == 1:
                pass
            elif self.country == 2:  # Andorra
                final_link += "&country=AD"
            elif self.country == 3:  # Afghanistan
                final_link += "&country=AF"
            elif self.country == 4:  # Albania
                final_link += "&country=AL"
            elif self.country == 5:  # Argentina
                final_link += "&country=AR"
            elif self.country == 6:  # Austria
                final_link += "&country=AT"
            elif self.country == 7:  # Australia
                final_link += "&country=AU"
            elif self.country == 8:  # Azerbaijan
                final_link += "&country=AZ"
            elif self.country == 9:  # Bosnia and Herzogvina
                final_link += "&country=BA"
            elif self.country == 10:  # Bangladesh
                final_link += "&country=BD"
            elif self.country == 11:  # Belgium
                final_link += "&country=BE"
            elif self.country == 12:  # Bulgaria
                final_link += "&country=BG"
            elif self.country == 13:  # Bolivia
                final_link += "&country=BE"
            elif self.country == 14:  # Brazil
                final_link += "&country=BR"
            elif self.country == 15:  # Botswana
                final_link += "&country=BW"
            elif self.country == 16:  # Belarus
                final_link += "&country=BY"
            elif self.country == 17:  # Canada
                final_link += "&country=CA"
            elif self.country == 18:  # Switzerland
                final_link += "&country=CH"
            elif self.country == 19:  # Chile
                final_link += "&country=CL"
            elif self.country == 20:  # China
                final_link += "&country=BE"
            elif self.country == 21:  # CN
                final_link += "&country=BE"
            elif self.country == 22:  # Colombia
                final_link += "&country=CO"
            elif self.country == 23:  # Costa Rika
                final_link += "&country=CR"
            elif self.country == 24:  # Cyprus
                final_link += "&country=CY"
            elif self.country == 25:  # Czechia
                final_link += "&country=CZ"
            elif self.country == 26:  # Germany
                final_link += "&country=DE"
            elif self.country == 27:  # Domincal Republic
                final_link += "&country=DO"
            elif self.country == 28:  # Ecuador
                final_link += "&country=EC"
            elif self.country == 29:  # Egypt
                final_link += "&country=EG"
            elif self.country == 30:  # Spain
                final_link += "&country=ES"
            elif self.country == 31:  # France
                final_link += "&country=FR"
            elif self.country == 32:  # United Kingdom
                final_link += "&country=GB"
            elif self.country == 33:  # Georgia
                final_link += "&country=GE"
            elif self.country == 34:  # Greece
                final_link += "&country=GR"
            elif self.country == 35:  # Guatemala
                final_link += "&country=GT"
            elif self.country == 36:  # Hong Kong
                final_link += "&country=HK"
            elif self.country == 37:  # Honduras
                final_link += "&country=HN"
            elif self.country == 38:  # Croatia
                final_link += "&country=HR"
            elif self.country == 39:  # Hungary
                final_link += "&country=HU"
            elif self.country == 40:  # Indonesia
                final_link += "&country=ID"
            elif self.country == 41:  # India
                final_link += "&country=IN"
            elif self.country == 42:  # Iraq
                final_link += "&country=IQ"
            elif self.country == 43:  # Iran
                final_link += "&country=IR"
            elif self.country == 44:  # Italy
                final_link += "&country=IT"
            elif self.country == 45:  # Kyrgzstan
                final_link += "&country=KG"
            elif self.country == 46:  # Cambodia
                final_link += "&country=KH"
            elif self.country == 47:  # Korea
                final_link += "&country=KR"
            elif self.country == 48:  # Kazakhasthan
                final_link += "&country=KZ"
            elif self.country == 49:  # Lebanon
                final_link += "&country=LB"
            elif self.country == 50:  # Sri Lanka
                final_link += "&country=LK"
            elif self.country == 51:  # Lithuania
                final_link += "&country=LT"
            elif self.country == 52:  # Moldova
                final_link += "&country=MD"
            elif self.country == 53:  # Mongolia
                final_link += "&country=MN"
            elif self.country == 54:  # Mexico
                final_link += "&country=MX"
            elif self.country == 55:  # Malaysia
                final_link += "&country=MY"
            elif self.country == 56:  # Mozambique
                final_link += "&country=MZ"
            elif self.country == 57:  # Nepal
                final_link += "&country=NP"
            elif self.country == 58:  # Panama
                final_link += "&country=PA"
            elif self.country == 59:  # Peru
                final_link += "&country=PE"
            elif self.country == 60:  # Philippines
                final_link += "&country=PH"
            elif self.country == 61:  # Pakistan
                final_link += "&country=PK"
            elif self.country == 62:  # Poland
                final_link += "&country=PL"
            elif self.country == 63:  # Palestine
                final_link += "&country=PS"
            elif self.country == 64:  # Portugal
                final_link += "&country=PT"
            elif self.country == 65:  # Romania
                final_link += "&country=RO"
            elif self.country == 66:  # Serbia
                final_link += "&country=RS"
            elif self.country == 67:  # Russia
                final_link += "&country=RU"
            elif self.country == 68:  # Rwanda
                final_link += "&country=RW"
            elif self.country == 69:  # Singapore
                final_link += "&country=MY"
            elif self.country == 70:  # Slovakia
                final_link += "&country=SK"
            elif self.country == 71:  # South Sudan
                final_link += "&country=SS"
            elif self.country == 72:  # Syrian Arabic Republic
                final_link += "&country=SY"
            elif self.country == 73:  # Thailand
                final_link += "&country=TH"
            elif self.country == 74:  # Turkey
                final_link += "&country=TR"
            elif self.country == 75:  # Ukraine
                final_link += "&country=UA"
            elif self.country == 76:  # United States
                final_link += "&country=US"
            elif self.country == 77:  # Vietnam
                final_link += "&country=VN"
            elif self.country == 78:  # South Africa
                final_link += "&country=ZA"
            elif self.country == 79:  # Zimbabwe
                final_link += "&country=ZW"

        # Uptime
        if self.uptime is not None:
            if self.uptime == 0:
                pass
            elif (self.uptime <= 10) and (self.uptime > 0):
                final_link += f"&filterLastChecked={self.uptime}"
            elif self.uptime >= 11:  # maybe change this to 'else'
                rounded = round(self.last_checked, -1)
                final_link += f"&filterLastChecked={rounded}"

        # Last Checked
        if self.uptime is not None:
            rounded = round(self.last_checked, -1)
            if rounded == 0:
                pass
            else:
                final_link += f"&filterUpTime={rounded}"

        # org and asn
        if (self.org_and_asn == 0) or (self.org_and_asn is None):
            pass
        elif self.org_and_asn == 1:
            final_link += "&filterByOrg=CONECTABR+SISTEMAS+DE+COMUNICA%C3%87%C3%95ES+LTDA"
        elif self.org_and_asn == 2:
            final_link += "&filterByOrg=Contabo+GmbH"
        elif self.org_and_asn == 3:
            final_link += "&filterByOrg=Cox+Communications+Inc."
        elif self.org_and_asn == 4:
            final_link += "&filterByOrg=Digital+Ocean"
        elif self.org_and_asn == 5:
            final_link += "&filterByOrg=DigitalOcean%2C+LLC"
        elif self.org_and_asn == 6:
            final_link += "&filterByOrg=Digitalocean"
        elif self.org_and_asn == 7:
            final_link += "&filterByOrg=Enforta-KGD"
        elif self.org_and_asn == 8:
            final_link += "&filterByOrg=Fransiskus"
        elif self.org_and_asn == 9:
            final_link += "&filterByOrg=Go+WiFi+Networking+Solutions+Pvt+Ltd"
        elif self.org_and_asn == 10:
            final_link += "&filterByOrg=Hetzner"
        elif self.org_and_asn == 11:
            final_link += "&filterByOrg=Hope+College"
        elif self.org_and_asn == 12:
            final_link += "&filterByOrg=JSC+%22ER-Telecom+Holding%22+Novosibirsk+branch"
        elif self.org_and_asn == 13:
            final_link += "&filterByOrg=Lanka+Communication+Services+%28Pvt%29+Ltd"
        elif self.org_and_asn == 14:
            final_link += "&filterByOrg=MFN-IP"
        elif self.org_and_asn == 15:
            final_link += "&filterByOrg=Melbikomas+UAB"
        elif self.org_and_asn == 16:
            final_link += "&filterByOrg=NET1"
        elif self.org_and_asn == 17:
            final_link += "&filterByOrg=NLT+Sub158"
        elif self.org_and_asn == 18:
            final_link += "&filterByOrg=Nedetel+S.A"
        elif self.org_and_asn == 19:
            final_link += "&filterByOrg=ONLINE"
        elif self.org_and_asn == 20:
            final_link += "&filterByOrg=OVH"
        elif self.org_and_asn == 21:
            final_link += "&filterByOrg=OVH+GmbH"
        elif self.org_and_asn == 22:
            final_link += "&filterByOrg=OVH+Hosting%2C+Inc"
        elif self.org_and_asn == 23:
            final_link += "&filterByOrg=Optinet+Telecomunica%C3%A7%C3%B5es+Ltda"
        elif self.org_and_asn == 24:
            final_link += "&filterByOrg=Pioneer+Elabs+Ltd."
        elif self.org_and_asn == 25:
            final_link += "&filterByOrg=RADIO"
        elif self.org_and_asn == 26:
            final_link += "&filterByOrg=RAN+Networks+S.L"
        elif self.org_and_asn == 27:
            final_link += "&filterByOrg=Reasonable+Software+House+Limited"
        elif self.org_and_asn == 28:
            final_link += "&filterByOrg=Suddenlink+Communications"
        elif self.org_and_asn == 29:
            final_link += "&filterByOrg=Superonline+Iletisim+Hizmetleri"
        elif self.org_and_asn == 30:
            final_link += "&filterByOrg=TheFirst"
        elif self.org_and_asn == 31:
            final_link += "&filterByOrg=Turk+Telekomunikasyon+A.S"
        elif self.org_and_asn == 32:
            final_link += "&filterByOrg=Vultr+Holdings%2C+LLC"

        return final_link

    def get_list(self):
        weblink = self.get_link()
        data_json = requests.get(weblink).json()
        return data_json["data"]

    def get_all_dicts(self):
        weblink = self.get_link()
        data_json = requests.get(weblink).json()
        for i in range(len(data_json["data"])):
            yield data_json["data"][i]

    def get_random_dict(self):
        weblink = self.get_link()
        data_json = requests.get(weblink).json()

        try:
            data_list = data_json["data"]
            return random.choice(data_list)
        except Exception as e:
            return f"Error: {e}"

    def get_proxies_only(self):
        weblink = self.get_link()
        data_json = requests.get(weblink).json()
        for i in range(len(data_json["data"])):
            yield f'{data_json["data"][i]["ip"]}:{data_json["data"][i]["port"]}'

    def get_data_json(self):
        weblink = self.get_link()
        data_json = requests.get(weblink).json()
        return data_json

    def get_data(self):
        weblink = self.get_link()
        rdata = requests.get(weblink)
        return rdata

    def get_request(self):
        weblink = self.get_link()
        rdata = requests.get(weblink)
        return rdata
