# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0.en.html).
{
    "name": "Lira",
    "summary": "Lira is frontend for project agile framework",
    "category": "Project",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar, Odoo Community Association (OCA)",
    "website": "https://www.modoolar.com/",
    "depends": [
        "project_agile",
        "web_syncer",
    ],

    "data": [
        # views
        "views/project_project_views.xml",
        "views/project_task_views.xml",
        "views/project_agile_team_views.xml",

        # Assets
        "views/lira.xml",
        "views/index.xml",

        # Menus
        "views/menu.xml",

        # data
        "data/project_task.xml",
    ],

    "demo": [
    ],

    "qweb": ["static/src/xml/*.xml"],
    "application": True,
    "installable": True,
}
