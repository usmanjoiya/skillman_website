from odoo import models, fields, api

class BlogPost(models.Model):
    _inherit = "blog.post"

    content_wo_html = fields.Char('Content Without html')