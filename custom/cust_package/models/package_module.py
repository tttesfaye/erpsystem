from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TestPackageModel(models.Model):
    _name = "test.package.model"
    _description = "this is a test package"

    name = fields.Char()
    location = fields.Char()
    startDate = fields.Date()


class Student(models.Model):
    _name = "test.student.model"
    _description = "this is a student"

    first_name = fields.Char()
    middle_name = fields.Char()
    last_name = fields.Char()
