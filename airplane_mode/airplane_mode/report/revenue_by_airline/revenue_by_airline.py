# Copyright (c) 2024, Soham Kulkarni and contributors
# For license information, please see license.txt

# import frappe
from frappe import _
import frappe

def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()
	chart = get_chart(data)
	return columns, data , None , chart


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Airline"),
			"fieldname": "airline",
			"fieldtype": "Data",
		},
		{
			"label": _("Revenue"),
			"fieldname": "revenue",
			"fieldtype": "Int",
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	tickets = frappe.get_list("Airplane Ticket")
	revenue_per_airline = {}
	for t in tickets:
		ticket = frappe.get_doc("Airplane Ticket", t)
		flight = frappe.get_doc("Airplane Flight",ticket.flight)
		airplane = frappe.get_doc("Airplane",flight.airplane)
		airline_name = airplane.airline
		ticket_amount =  ticket.total_amount

		if airline_name not in revenue_per_airline:
        		revenue_per_airline[airline_name] = 0
    
		revenue_per_airline[airline_name] += ticket_amount
	


	airlines  = frappe.get_list("Airline")
	for a in airlines:
		if a.name not in revenue_per_airline:
			revenue_per_airline[a.name] = 0
	
	revenue_list = [[airline, revenue] for airline, revenue in revenue_per_airline.items()]

	return revenue_list


def get_chart(data):
	labels = []
	values = []
	for i in data:
		labels.append(i[0])
		values.append(i[1])
	chart = {
		'data':{
		'labels':labels,
		'datasets':[
			{'values':values}
		]
		},
		'type':'donut'
	}
	return chart