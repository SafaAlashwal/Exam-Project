import frappe
from frappe import _

def get_context(context):
    doc_list = frappe.get_list("Question")
    context.doc_list = doc_list
    return context

def save_word():
    doc = frappe.new_doc("AnotherDocType")
    doc.word = "hello"
    doc.save()

def get_route():
    return "/review_exam"

