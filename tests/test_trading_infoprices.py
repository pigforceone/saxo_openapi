#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `saxo_openapi` package."""

import sys
import unittest
from . import unittestsetup
from .unittestsetup import environment, mock_env, test_generic
from saxo_openapi import API
import saxo_openapi.endpoints.trading as tr
import requests_mock
from nose_parameterized import parameterized


access_token = None
api = None


class TestSaxo_Trading_InfoPrices(unittest.TestCase):
    """Tests for `trading-prices` endpoints."""

    def setUp(self):
        """Set up test fixtures, if any."""
        global access_token
        global api

        try:
            access_token = unittestsetup.auth()
            setattr(sys.modules["saxo_openapi.saxo_openapi"],
                    "TRADING_ENVIRONMENTS",
                    mock_env)
            api = API(environment=environment, access_token=access_token)
            api.api_url = 'https://test.com'

        except Exception as e:
            print(e)
            exit(0)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @parameterized.expand([
        (tr.infoprices, "InfoPrice", {}),
        (tr.infoprices, "InfoPrices", {}),
        (tr.infoprices, "CreateInfoPriceSubscription", {}),
        (tr.infoprices, "RemoveInfoPriceSubscriptionsByTag",
                        {'ContextId': 'ctxt_20190316'}),
        (tr.infoprices, "RemoveInfoPriceSubscriptionById",
                        {'ContextId': 'ctxt_20190316',
                         'ReferenceId': 'pri_EURUSD'}),
      ])
    @requests_mock.Mocker(kw='mock')
    def test__rd_all(self, _mod, clsNm, route, **kwargs):
        test_generic(self, api, _mod, clsNm, route, **kwargs)


if __name__ == "__main__":

    unittest.main()