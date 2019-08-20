
import json
import math
import rlp
from common.load_file import LoadFile
from hexbytes import HexBytes
from client_sdk_python.eth import Eth
from conf import setting as conf
from common.connect import connect_web3
from client_sdk_python import (
    Web3,
)
import random
#初始token
von= 10000000000

von1 = von*(1+0.025)
von2 = von*(1+0.025)*(1+0.025)
von3 = von*(1+0.025)*(1+0.025)*(1+0.025)