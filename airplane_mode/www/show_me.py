import frappe

sitemap = 1


def get_context(context):
        params = frappe.form_dict
        context.color = "black"
        if(params.color):
                context.color = params.color
        return context