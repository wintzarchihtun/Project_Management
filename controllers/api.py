from odoo import http
from odoo.http import request


class Project(http.Controller):

    @http.route('/project/project_task/', auth='user', website=True)
    def project_task(self, **kw):
        a = request.env['project.task'].sudo().search([])

        return request.render('project.project_page', {'a': a})

    @http.route('/project/create_project', auth='user', type='json')
    def create_project(self, **rec):
        if request.jsonrequest:
            print(rec)
            if rec['name']:
                vals = {
                    'name': rec['name']
                }
                new_project = request.env['project.project'].sudo().create([vals])
                args = {'success': True, 'message': 'Success', 'ID': new_project.id}

        return args

    @http.route('/api/project_task', type='json', auth='user')
    def get_project(self, **kw):

        print('Yes Get Data')

        project_rec = request.env['project.task'].search([])
        project = []
        for a in project_rec:
            vals = {
                'id': a.id,
                'name': a.name,
                'progress':a.progress,

            }
            project.append(vals)
            print(project)
        data = {'status': 200, 'response': project, 'message': 'Success'}
        return data

    @http.route('/api/project_name', type='json', auth='user')
    def get_projecttask(self, **kw):
        project_rec = request.env['project.project'].search([])
        project_task = []
        for rec in project_rec:
            vals = {

                'id': rec.id,
                'name': rec.name,

            }
            project_task.append(vals)
        data = {'status': 200, 'response': project_task, 'message': 'Success'}
        return data
#
# # # #
# # class Task(http.Controller):
# #     @http.route('/api/task/', auth='public', website=True)
# #     def hospital_patient(self, **kw):
# #         patients = request.env['project.task'].sudo().search([])
# #         task = []
# #         for rec in patients:
# #             vals = {
# #                 'id': rec.id,
# #                 'name': rec.name,
# #             }
# #             task.append(vals)
# #         data = {'status': 200, 'response': task, 'message': success}
# #         return data
# #
# #         return 'Hello Zaw Naing Linn'
