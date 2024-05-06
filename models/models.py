# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import xmlrpc.client
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from odoo import api, models
import logging
_logger = logging.getLogger(__name__)

url = 'http://194.163.185.47:8003'
db_name = 'skillman_09'
username = 'admin'
password = 'admin'


class BlogPostInherit(models.Model):
    _inherit = "blog.post"

    def create_blogs(self):
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db_name, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        remote_blogs = models.execute_kw(db_name, uid, password, 'blog.post', 'search_read', [[]],
                                         {'fields': ['name', 'content', 'author_id', 'published_date', 'published_date','blog_id', 'tag_ids', 'subtitle', 'write_uid', 'website_meta_title'],})

        for remote_blog in remote_blogs:
            author_id = self.env['res.partner'].sudo().search([('name', '=', remote_blog['author_id'][1])], limit=1)
            if not author_id:
                author_id = self.env['res.partner'].create({
                    'name': remote_blog['author_id'][1],
                })
            blog_id = self.env['blog.blog'].sudo().search([('name', '=', remote_blog['blog_id'][1])], limit=1)
            if not blog_id:
                blog_id = self.env['blog.blog'].create({
                    'name': remote_blog['blog_id'][1],
                })
            local_blog = self.create({
                'name': remote_blog['name'],
                'blog_id': blog_id.id,
                'content': remote_blog['content'],
                'author_id': author_id.id,
                'published_date': remote_blog['published_date'],
                'subtitle': remote_blog['subtitle'],
                'website_meta_title': remote_blog['website_meta_title'],
                'tag_ids': remote_blog['tag_ids'],
                'write_uid': remote_blog['blog_id'][1] if remote_blog['blog_id'][1] else False,
            })
            _logger.info("Created blog in local database with ID: %s", local_blog.id)
