"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'tallykhata-backend.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Portal Access Management'),
            column=1,
            collapsible=False,
            models=('django.contrib.auth.models.User',),
        ))

        self.children.append(modules.Group(
            _('ChatApp Data'),
            column=1,
            collapsible=True,
            children=[
                modules.ModelList(
                    _('Rooms'),
                    column=1,
                    collapsible=False,
                    models=('chatApp.models.Room',),
                ),
                modules.ModelList(
                    _('Messages'),
                    column=1,
                    collapsible=False,
                    models=('chatApp.models.Message',),
                ),
            ],
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Other links'),
            column=3,
            children=[
                {
                    'title': _('DjangoChat Project Github URL'),
                    'url': 'https://github.com/RatedRAkash/Django_Chat_Application',
                    'external': True,
                    'target': '_blank'
                },
            ]
        ))
