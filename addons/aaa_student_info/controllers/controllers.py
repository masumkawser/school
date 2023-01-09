# -*- coding: utf-8 -*-
# from odoo import http


# class AaaStudentInfo(http.Controller):
#     @http.route('/aaa_student_info/aaa_student_info', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aaa_student_info/aaa_student_info/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aaa_student_info.listing', {
#             'root': '/aaa_student_info/aaa_student_info',
#             'objects': http.request.env['aaa_student_info.aaa_student_info'].search([]),
#         })

#     @http.route('/aaa_student_info/aaa_student_info/objects/<model("aaa_student_info.aaa_student_info"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aaa_student_info.object', {
#             'object': obj
#         })
