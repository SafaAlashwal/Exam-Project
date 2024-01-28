# Copyright (c) 2024, Exam Managment and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Collage(Document):
	def create_collage(self):
		self.name1 = "jjj"
		self.insert()
		frappe.msgprint("done")