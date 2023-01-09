# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class aaa_student_info(models.Model):
#     _name = 'aaa_student_info.aaa_student_info'
#     _description = 'aaa_student_info.aaa_student_info'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
