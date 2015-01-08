# -*- coding: utf-8 -*-


from openerp.osv import osv
from openerp.tools.translate import _


class project_project (osv.Model):

    _inherit = 'project.project'

    _defaults = {
        'use_timesheets': True,
    }

#    def _get_visibility_selection(self, cr, uid, context=None):
#        """ Overriden in portal_project to offer more options """
#        return [('public', 'Public project'),
#                ('employees', 'Internal project: all employees can access'),
#                #('team', 'Team project: only team members can access'),
#                ('followers', 'Private project: followers Only')]
#
