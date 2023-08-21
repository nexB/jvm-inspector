# -*- coding: utf-8 -*-
#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/jvm-inspector for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#


import attr
from commoncode.cliutils import SCAN_GROUP
from commoncode.cliutils import PluggableCommandLineOption
from plugincode.scan import ScanPlugin
from plugincode.scan import scan_impl

from jvm_inspector.jvm import get_java_package


@scan_impl
class JavaPackageScanner(ScanPlugin):
    """
    Scan a .java file for its Java package.
    """

    resource_attributes = dict(java_package=attr.ib(default=None, repr=False))

    options = [
        PluggableCommandLineOption(
            ("--java-package",),
            is_flag=True,
            default=False,
            help="Collect the Java package of Java source code file.",
            help_group=SCAN_GROUP,
            sort_order=100,
        ),
    ]

    def is_enabled(self, java_package, **kwargs):
        return java_package

    def get_scanner(self, **kwargs):
        return get_java_package
