# -*- coding: utf-8 -*-

import json
import math
import time
import random

import allure
import pytest
from client_sdk_python import Web3
from utils.platon_lib.ppos import Ppos
from conf import  setting as conf
from common.load_file import get_node_list
from common import log
import json
from common.connect import connect_web3
from utils.platon_lib.govern_util import *
from utils.platon_lib.ppos_common import CommonMethod
from deploy.deploy import AutoDeployPlaton

class TestPunishment():

    address = conf.ADDRESS
    pwd = conf.PASSWORD
    abi = conf.DPOS_CONTRACT_ABI
    cbft_json_path = conf.CBFT2
    node_yml_path = conf.PPOS_NODE_TEST_YML
    file = conf.CASE_DICT
    privatekey = conf.PRIVATE_KEY
    base_gas_price = 60000000000000
    base_gas = 21000
    staking_gas = base_gas + 32000 + 6000 + 100000
    transfer_gasPrice = Web3.toWei (1, 'ether')
    transfer_gas = 210000000
    value = 1000
    chainid = 120
    ConsensusSize = 150
    time_interval = 10
    initial_amount = {'FOUNDATION': 905000000000000000000000000,
                      'FOUNDATIONLOCKUP': 20000000000000000000000000,
                      'STAKING': 25000000000000000000000000,
                      'INCENTIVEPOOL': 45000000000000000000000000,
                      'DEVELOPERS': 5000000000000000000000000
                      }

    def test_duplicate_Sign(self):
        nodeId = CommonMethod.get_no_candidate_list (self)
        url = CommonMethod.link_list (self)
        platon_ppos = Ppos (url, self.address, self.chainid)

        #举报双签


