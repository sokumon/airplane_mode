// Copyright (c) 2024, Soham Kulkarni and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        const stream_link = frm.doc.website;
        console.log("weblink", stream_link)
        if(weblink){
            frm.add_web_link(stream_link, "Airline site");
        }

	},
});
