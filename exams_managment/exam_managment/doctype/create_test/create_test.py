# Copyright (c) 2023, Exam Managment and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CreateTest(Document):
 @frappe.whitelist()
 def addtest(self):
  doc=frappe.new_doc("Review Test")
  doc.collage=self.collage
  doc.department=self.department
  doc.level=self.level
  doc.subject=self.subject
  doc.question=self.question
  doc.test_type=self.test_type
  doc.test_degree=self.test_degree
  doc.insert()
  frappe.msgprint("done")
