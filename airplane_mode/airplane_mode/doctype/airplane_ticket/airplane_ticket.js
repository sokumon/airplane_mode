// Copyright (c) 2024, Soham Kulkarni and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button(__('Assign a seat'), function() {
            frappe.prompt('Seat',setSeat, 'Seat Number', 'Submit');

        }, __("Actions"));
	},
});

function setSeat(seat){
    console.log(seat)
    cur_frm.set_value("seat",seat.value)
}