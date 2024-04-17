# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SkillmanWebsite(http.Controller):
    @http.route('/', auth='public', type='http', website=True)
    def home(self, **kw):
        values = {
            'blogs': request.env['blog.post'].search([], limit=6)
        }
        return http.request.render('skillman_website.home', values)

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

    @http.route('/submit-your-candidature', auth='public', type='http', website=True)
    def submit(self, **kw):
        return http.request.render('skillman_website.submit_your_candidature')

    @http.route('/awards-candidatures', auth='public', type='http', website=True)
    def awards_candidatures(self, **kw):
        return http.request.render('skillman_website.awards-candidatures')

    @http.route('/awards-2', auth='public', type='http', website=True)
    def awards(self, **kw):
        return http.request.render('skillman_website.awards_2')

    @http.route('/timeline', auth='public', type='http', website=True)
    def timeline(self, **kw):
        return http.request.render('skillman_website.timeline')

    @http.route('/include-skillman-in-a-new-project-partnership', auth='public', type='http', website=True)
    def partnership(self, **kw):
        return http.request.render('skillman_website.include_skillman_in_a_new_project_partnership')

    @http.route('/submit-your-idea', auth='public', type='http', website=True)
    def idea(self, **kw):
        return http.request.render('skillman_website.submit_your_idea')

    @http.route('/skillnet-management-platform', auth='public', type='http', website=True)
    def smp(self, **kw):
        return http.request.render('skillman_website.skillnet_management_platform')

    @http.route('/skillnet-2022', auth='public', type='http', website=True)
    def skillnet(self, **kw):
        return http.request.render('skillman_website.skillnet_2022')

    @http.route('/gender-equality', auth='public', type='http', website=True)
    def gender(self, **kw):
        return http.request.render('skillman_website.gender')

    @http.route('/as2023', auth='public', type='http', website=True)
    def ass3(self, **kw):
        return http.request.render('skillman_website.as2023')

    @http.route('/as2022', auth='public', type='http', website=True)
    def ass2(self, **kw):
        return http.request.render('skillman_website.as2022')

    @http.route('/sif2022', auth='public', type='http', website=True)
    def sif2(self, **kw):
        return http.request.render('skillman_website.sif2022')

    @http.route('/sif2021', auth='public', type='http', website=True)
    def sif1(self, **kw):
        return http.request.render('skillman_website.sif2021')

    @http.route('/sif2020', auth='public', type='http', website=True)
    def sif0(self, **kw):
        return http.request.render('skillman_website.sif2020')

    @http.route('/e-newsletter', auth='public', type='http', website=True)
    def e_newsletter(self, **kw):
        return http.request.render('skillman_website.e_newsletter')

    @http.route('/skillman-youth-forum', auth='public', type='http', website=True)
    def skillman_youth_forum(self, **kw):
        return http.request.render('skillman_website.skillman_youth_forum')

    @http.route('/ethical-campaign-to-redefine-the-future-of-learning', auth='public', type='http', website=True)
    def ethical_campaign_to_redefine_the_future_of_learning(self, **kw):
        return http.request.render('skillman_website.ethical_campaign_to_redefine_the_future_of_learning')

    @http.route('/peer-learning-club-1-advanced-manufacturing-sector-publication', auth='public', type='http',
                website=True)
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

    @http.route('/skillman-advisory-service', auth='public', type='http', website=True)
    def skillman_advisory_service(self, **kw):
        return http.request.render('skillman_website.skillman_advisory_service')

    @http.route('/webinars-catalog', auth='public', type='http', website=True)
    def webinars_catalog(self, **kw):
        return http.request.render('skillman_website.webinars_catalog')

    @http.route('/skillman-technical-webinars', auth='public', type='http', website=True)
    def skillman_technical_webinars(self, **kw):
        return http.request.render('skillman_website.skillman_technical_webinars')

    @http.route('/webinars-on-eu-fund-opportunities', auth='public', type='http', website=True)
    def webinars_on_eu_fund_opportunities(self, **kw):
        return http.request.render('skillman_website.webinars_on_eu_fund_opportunities')

    @http.route('/peer-learning-clubs', auth='public', type='http', website=True)
    def peer_learning_clubs(self, **kw):
        return http.request.render('skillman_website.peer_learning_clubs')

    @http.route('/skillman-eu-international-forum-2018', auth='public', type='http', website=True)
    def skillman_eu_international_forum_2018(self, **kw):
        return http.request.render('skillman_website.skillman_eu_international_forum_2018')

    @http.route('/skillman-eu-international-forum-2019', auth='public', type='http', website=True)
    def skillman_eu_international_forum_2019(self, **kw):
        return http.request.render('skillman_website.skillman_eu_international_forum_2019')

    @http.route('/tvet-digital-triathlon', auth='public', type='http', website=True)
    def tvet_digital_triathlon(self, **kw):
        return http.request.render('skillman_website.tvet_digital_triathlon')

    @http.route('/skillman-at-the-european-skills-week-2020', auth='public', type='http', website=True)
    def skillman_at_the_european_skills_week_2020(self, **kw):
        return http.request.render('skillman_website.skillman_at_the_european_skills_week_2020')

    @http.route('/second-international-conference', auth='public', type='http', website=True)
    def second_international_conference(self, **kw):
        return http.request.render('skillman_website.second_international_conference')

    @http.route('/2015-international-conference', auth='public', type='http', website=True)
    def international_conference_2015(self, **kw):
        return http.request.render('skillman_website.2015_international_conference')

    @http.route('/2016-international-conference', auth='public', type='http', website=True)
    def international_conference_2016(self, **kw):
        return http.request.render('skillman_website.2016_international_conference')

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

    @http.route('/bmet', auth='public', type='http', website=True)
    def bmet(self, **kw):
        return http.request.render('skillman_website.bmet')

    @http.route('/cepas', auth='public', type='http', website=True)
    def cepas(self, **kw):
        return http.request.render('skillman_website.cepas')

    @http.route('/cnr', auth='public', type='http', website=True)
    def cnr(self, **kw):
        return http.request.render('skillman_website.cnr')

    @http.route('/crf', auth='public', type='http', website=True)
    def crf(self, **kw):
        return http.request.render('skillman_website.crf')

    @http.route('/cscs', auth='public', type='http', website=True)
    def cscs(self, **kw):
        return http.request.render('skillman_website.cscs')

    @http.route('/eal', auth='public', type='http', website=True)
    def eal(self, **kw):
        return http.request.render('skillman_website.eal')

    @http.route('/eef', auth='public', type='http', website=True)
    def eef(self, **kw):
        return http.request.render('skillman_website.eef')

    @http.route('/iu', auth='public', type='http', website=True)
    def iu(self, **kw):
        return http.request.render('skillman_website.iu')

    @http.route('/jlr', auth='public', type='http', website=True)
    def jlr(self, **kw):
        return http.request.render('skillman_website.jlr')

    @http.route('/sas', auth='public', type='http', website=True)
    def sas(self, **kw):
        return http.request.render('skillman_website.sas')

    @http.route('/skillnet-events', auth='public', type='http', website=True)
    def skillnet_events(self, **kw):
        return http.request.render('skillman_website.skillnet_events')

    @http.route('/tec-5', auth='public', type='http', website=True)
    def tc_5(self, **kw):
        return http.request.render('skillman_website.tc_5')

    @http.route('/ambassadors', auth='public', type='http', website=True)
    def ambassadors(self, **kw):
        return http.request.render('skillman_website.ambassadors')

    @http.route('/members-list', auth='public', type='http', website=True)
    def members_list(self, **kw):
        return http.request.render('skillman_website.members_list')

    @http.route('/members', auth='public', type='http', website=True)
    def members(self, **kw):
        return http.request.render('skillman_website.members')

    @http.route('/new-event', auth='public', type='http', website=True)
    def new_event(self, **kw):
        return http.request.render('skillman_website.new_event')

    @http.route('/the-conference', auth='public', type='http', website=True)
    def the_conference(self, **kw):
        return http.request.render('skillman_website.the_conference')

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
