app_name = "ignore_deletion_doctype"
app_title = "Ignore Deletion Doctype"
app_publisher = "mina"
app_description = "mina"
app_email = "mina@email.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ignore_deletion_doctype",
# 		"logo": "/assets/ignore_deletion_doctype/logo.png",
# 		"title": "Ignore Deletion Doctype",
# 		"route": "/ignore_deletion_doctype",
# 		"has_permission": "ignore_deletion_doctype.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ignore_deletion_doctype/css/ignore_deletion_doctype.css"
# app_include_js = "/assets/ignore_deletion_doctype/js/ignore_deletion_doctype.js"

# include js, css files in header of web template
# web_include_css = "/assets/ignore_deletion_doctype/css/ignore_deletion_doctype.css"
# web_include_js = "/assets/ignore_deletion_doctype/js/ignore_deletion_doctype.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ignore_deletion_doctype/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ignore_deletion_doctype/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

#####################IGNORE DELETION DOCTYPE############################

company_data_to_be_ignored=[
    "Salary Structure",
    "Salary Slip",
    "Salary Structure Assignment",
    "Department",
    "Leave Allocation",
    "Salary Component",
    "Income Tax Slab",
    "Additional Salary",
    "Effected salaries",
    "Permission",
    "Attendance",
    "Payroll Period",
    "Leave Period",
    "Job Opening",
    "Shift Assignment",
    "Leave Application"
] ###Mina & Eng Ahmed####








# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ignore_deletion_doctype.utils.jinja_methods",
# 	"filters": "ignore_deletion_doctype.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ignore_deletion_doctype.install.before_install"
# after_install = "ignore_deletion_doctype.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ignore_deletion_doctype.uninstall.before_uninstall"
# after_uninstall = "ignore_deletion_doctype.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ignore_deletion_doctype.utils.before_app_install"
# after_app_install = "ignore_deletion_doctype.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ignore_deletion_doctype.utils.before_app_uninstall"
# after_app_uninstall = "ignore_deletion_doctype.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ignore_deletion_doctype.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ignore_deletion_doctype.tasks.all"
# 	],
# 	"daily": [
# 		"ignore_deletion_doctype.tasks.daily"
# 	],
# 	"hourly": [
# 		"ignore_deletion_doctype.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ignore_deletion_doctype.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ignore_deletion_doctype.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ignore_deletion_doctype.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ignore_deletion_doctype.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ignore_deletion_doctype.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ignore_deletion_doctype.utils.before_request"]
# after_request = ["ignore_deletion_doctype.utils.after_request"]

# Job Events
# ----------
# before_job = ["ignore_deletion_doctype.utils.before_job"]
# after_job = ["ignore_deletion_doctype.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ignore_deletion_doctype.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

