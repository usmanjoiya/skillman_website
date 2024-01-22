# -*- coding: utf-8 -*-
from odoo import http


class SkillmanWebsite(http.Controller):
    @http.route('/', auth='public', type='http', website=True)
    def home(self, **kw):
        return http.request.render('skillman_website.home')

    @http.route('/lifecycle-concept', auth='public', type='http', website=True)
    def lifecycle(self, **kw):
        return http.request.render('skillman_website.lifecycle-concept')

    @http.route('/skills', auth='public', type='http', website=True)
    def skill(self, **kw):
        return http.request.render('skillman_website.skill')

    @http.route('/memorandum-of-understanding', auth='public', type='http', website=True)
    def memorandum(self, **kw):
        return http.request.render('skillman_website.memorandum-of-understanding')

    @http.route('/eqavet_european_quality_assurance_in_vet-2', auth='public', type='http', website=True)
    def ecvet(self, **kw):
        return http.request.render('skillman_website.eqavet_european_quality_assurance_in_vet-2')

    @http.route('/eqavet_european_quality_assurance_in_vet-2-2', auth='public', type='http', website=True)
    def ecvet2(self, **kw):
        return http.request.render('skillman_website.eqavet_european_quality_assurance_in_vet-2-2')

    @http.route('/eqavet_european_quality_assurance_in_vet', auth='public', type='http', website=True)
    def ecvet3(self, **kw):
        return http.request.render('skillman_website.eqavet_european_quality_assurance_in_ve')

    @http.route('/esco_skills_competencies_occupations', auth='public', type='http', website=True)
    def esco(self, **kw):
        return http.request.render('skillman_website.esco_skills_competencies_occupations')

    @http.route('/submit_your_candidature', auth='public', type='http', website=True)
    def submit(self, **kw):
        return http.request.render('skillman_website.submit_your_candidature')

    @http.route('/awards_2', auth='public', type='http', website=True)
    def awards(self, **kw):
        return http.request.render('skillman_website.awards_2')

    @http.route('/timeline', auth='public', type='http', website=True)
    def timeline(self, **kw):
        return http.request.render('skillman_website.timeline')

    @http.route('/include_skillman_in_a_new_project_partnership', auth='public', type='http', website=True)
    def partnership(self, **kw):
        return http.request.render('skillman_website.include_skillman_in_a_new_project_partnership')

    @http.route('/submit_your_idea', auth='public', type='http', website=True)
    def idea(self, **kw):
        return http.request.render('skillman_website.submit_your_idea')

    @http.route('/skillnet_management_platform', auth='public', type='http', website=True)
    def smp(self, **kw):
        return http.request.render('skillman_website.skillnet_management_platform')

    @http.route('/skillnet_2022', auth='public', type='http', website=True)
    def skillnet(self, **kw):
        return http.request.render('skillman_website.skillnet_2022')

    @http.route('/gender_equality', auth='public', type='http', website=True)
    def gender(self, **kw):
        return http.request.render('skillman_website.gender')

    @http.route('/as2023', auth='public', type='http', website=True)
    def ass(self, **kw):
        return http.request.render('skillman_website.as2023')

    @http.route('/e_newsletter', auth='public', type='http', website=True)
    def e_newsletter(self, **kw):
        return http.request.render('skillman_website.e_newsletter')

    @http.route('/skillman_youth_forum', auth='public', type='http', website=True)
    def skillman_youth_forum(self, **kw):
        return http.request.render('skillman_website.skillman_youth_forum')

    @http.route('/ethical_campaign_to_redefine_the_future_of_learning', auth='public', type='http', website=True)
    def ethical_campaign_to_redefine_the_future_of_learning(self, **kw):
        return http.request.render('skillman_website.ethical_campaign_to_redefine_the_future_of_learning')

    @http.route('/peer-learning-club-1-advanced-manufacturing-sector-publication', auth='public', type='http', website=True)
    def learning_club1(self, **kw):
        return http.request.render('skillman_website.peer-learning-club-1-advanced-manufacturing-sector-publication')

    @http.route('/peer-learning-club-2-advocacy-policy-influencing', auth='public', type='http', website=True)
    def learning_club2(self, **kw):
        return http.request.render('skillman_website.peer-learning-club-2-advocacy-policy-influencing')

    @http.route('/peer-learning-club-3-work-based-learning-and-standards', auth='public', type='http', website=True)
    def learning_club3(self, **kw):
        return http.request.render('skillman_website.peer-learning-club-3-work-based-learning-and-standards')

    @http.route('/peer-learning-club-4-train-the-trainers', auth='public', type='http', website=True)
    def learning_club4(self, **kw):
        return http.request.render('skillman_website.peer-learning-club-4-train-the-trainers')

    @http.route('/skillman_advisory_service', auth='public', type='http', website=True)
    def skillman_advisory_service(self, **kw):
        return http.request.render('skillman_website.skillman_advisory_service')

    @http.route('/skillman_advisory_service', auth='public', type='http', website=True)
    def skillman_advisory_service(self, **kw):
        return http.request.render('skillman_website.skillman_advisory_service')

    @http.route('/tvet_digital_triathlon', auth='public', type='http', website=True)
    def tvet_digital_triathlon(self, **kw):
        return http.request.render('skillman_website.tvet_digital_triathlon')

    @http.route('/skillman_at_the_european_skills_week_2020', auth='public', type='http', website=True)
    def skillman_at_the_european_skills_week_2020(self, **kw):
        return http.request.render('skillman_website.skillman_at_the_european_skills_week_2020')

    @http.route('/2015_international_conference', auth='public', type='http', website=True)
    def international_conference_2015(self, **kw):
        return http.request.render('skillman_website.2015_international_conference')

    @http.route('/2016_international_conference', auth='public', type='http', website=True)
    def international_conference_2016(self, **kw):
        return http.request.render('skillman_website.2016_international_conference')

    @http.route('/second_international_conference', auth='public', type='http', website=True)
    def second_international_conference(self, **kw):
        return http.request.render('skillman_website.second_international_conference')

    @http.route('/why', auth='public', type='http', website=True)
    def why(self, **kw):
        return http.request.render('skillman_website.why')

    @http.route('/contacts', auth='public', type='http', website=True)
    def contacts(self, **kw):
        return http.request.render('skillman_website.contacts')

    @http.route('/partners', auth='public', type='http', website=True)
    def partners(self, **kw):
        return http.request.render('skillman_website.partners')

    @http.route('/news', auth='public', type='http', website=True)
    def news(self, **kw):
        return http.request.render('skillman_website.news')

    @http.route('/focus', auth='public', type='http', website=True)
    def focus(self, **kw):
        return http.request.render('skillman_website.focus')


#     @http.route('/skillman_website/skillman_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('skillman_website.listing', {
#             'root': '/skillman_website/skillman_website',
#             'objects': http.request.env['skillman_website.skillman_website'].search([]),
#         })

#     @http.route('/skillman_website/skillman_website/objects/<model("skillman_website.skillman_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('skillman_website.object', {
#             'object': obj
#         })
