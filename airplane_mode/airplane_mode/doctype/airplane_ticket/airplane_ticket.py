# Copyright (c) 2024, Soham Kulkarni and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random


class AirplaneTicket(Document):
	def validate(self):
		self.find_unique_add_ons()
		self.calculate_total_amount()

	def find_unique_add_ons(self):
		prev_add_on = None
		final_add_ons = []
		for a in self.add_ons:
			if prev_add_on is None or prev_add_on.item != a.item:
					final_add_ons.append(a)
			prev_add_on = a  
		
		print(final_add_ons)

		self.add_ons = final_add_ons

			
		
	def calculate_total_amount(self):
		total_add_on_amount = 0
		for a in self.add_ons:
			total_add_on_amount = total_add_on_amount + a.amount
		self.total_amount = int(self.flight_price) +  total_add_on_amount

	def on_submit(self):
		if self.status != "Boarded":
			frappe.throw("Set the status to Boarded")

		#  adding a seat
		number_val = random.randint(1,101)
		letter = chr(random.randint(65,70))
		self.seat = f"{number_val}{letter}"