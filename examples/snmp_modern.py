from pysnmp.hlapi.asyncio import CommunityData as AsyncCommunity
from pysnmp.hlapi.asyncio import UsmUserData as AsyncUser
from pysnmp.hlapi.v1arch import CommunityData as V1Community
from pysnmp.hlapi.v1arch.asyncio import CommunityData as V1AsyncCommunity
from pysnmp.hlapi.v1arch.asyncio.auth import CommunityData as V1AuthCommunity
from pysnmp.hlapi.v3arch import CommunityData as V3Community
from pysnmp.hlapi.v3arch import UsmUserData as V3User
from pysnmp.hlapi.v3arch.asyncio import CommunityData as V3AsyncCommunity
from pysnmp.hlapi.v3arch.asyncio import UsmUserData as V3AsyncUser
from pysnmp.hlapi.v3arch.asyncio.auth import CommunityData as V3AuthCommunity
from pysnmp.hlapi.v3arch.asyncio.auth import UsmUserData as V3AuthUser
from unrelated import CommunityData, UsmUserData

# SHOULD FAIL: SNMPv1 and SNMPv2c through each modern import path.
AsyncCommunity("public", mpModel=0)
V1Community("public", mpModel=1)
V1AsyncCommunity("public", mpModel=0)
V1AuthCommunity("public", mpModel=1)
V3Community("public", mpModel=0)
V3AsyncCommunity("public", mpModel=1)
V3AuthCommunity("public", mpModel=0)

# SHOULD FAIL: SNMPv3 without privacy through each modern import path.
AsyncUser("user")
V3User("user", "auth")
V3AsyncUser("user")
V3AuthUser("user", "auth")

# SHOULD PASS: existing argument handling and unrelated classes stay unchanged.
AsyncUser("user", "auth", "priv")
V3User("user", "auth", "priv")
V3AsyncUser("user", "auth", "priv")
V3AuthUser("user", "auth", "priv")
CommunityData("public", mpModel=0)
UsmUserData("user")
