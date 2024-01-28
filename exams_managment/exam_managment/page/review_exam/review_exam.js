frappe.pages['review-exam'].on_page_load = function (wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Review Exam',
		single_column: true
	});

	// Create a button for the print command
	page.add_inner_button('Prints', function () {
		// Add your print logic here
		frappe.call({
			method: "addtest",
			callback: () => {
				frappe.msgprint("done")
			}

		})
		frappe.msgprint('Print command clicked');
	});
	$(frappe.render_template("review_exam", {})).appendTo(page.body);

};