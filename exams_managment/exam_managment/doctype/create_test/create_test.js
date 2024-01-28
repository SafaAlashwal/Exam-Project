// Copyright (c) 2024, Exam Managment and contributors
// For license information, please see license.txt

frappe.ui.form.on('Create Test', {
	after_save(frm) {
		frappe.call({
			method: "addtest",
			doc: frm.doc,
			callback: () => {
				frappe.msgprint("done")
			}
		})
	}
});
