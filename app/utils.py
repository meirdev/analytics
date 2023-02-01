import IP2Location
from ua_parser import user_agent_parser

from .schemes import FullUserAgent, IPInfo
from .settings import settings

ip_database = IP2Location.IP2Location(settings.ip2location_bin)


def get_ip_info(ip: str) -> IPInfo:
    ip_info = ip_database.get_all(ip)
    return IPInfo.parse_obj(ip_info.__dict__)


def get_user_agent(user_agent: str) -> FullUserAgent:
    user_agent_parsed = user_agent_parser.Parse(user_agent)
    return FullUserAgent.parse_obj(user_agent_parsed)
