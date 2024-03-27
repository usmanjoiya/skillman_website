# -*- coding: utf-8 -*-
{
    'name': "skillman_website",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','website_blog'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/header.xml',
        'data/footer.xml',
        'data/index.xml',
        'data/lifecycle_concept.xml',
        'data/skills.xml',
        'data/memorandum-of-understanding.xml',
        'data/eqavet_european_quality_assurance_in_vet-2.xml',
        'data/eqavet_european_quality_assurance_in_vet-2-2.xml',
        'data/eqavet_european_quality_assurance_in_ve.xml',
        'data/esco_skills_competencies_occupations.xml',
        'data/submit_your_candidature.xml',
        'data/awards_2.xml',
        'data/skillman_youth_forum.xml',
        'data/timeline.xml',
        'data/include_skillman_in_a_new_project_partnership.xml',
        'data/submit_your_idea.xml',
        'data/skillnet_management_platform.xml',
        'data/skillnet_2022.xml',
        'data/gender_equality.xml',
        'data/as2022.xml',
        'data/as2023.xml',
        'data/sif2022.xml',
        'data/sif2021.xml',
        'data/sif2020.xml',
        'data/e_newsletter.xml',
        'data/ethical_campaign_to_redefine_the_future_of_learning.xml',
        'data/peer-learning-club-1-advanced-manufacturing-sector-publication.xml',
        'data/peer-learning-club-2-advocacy-policy-influencing.xml',
        'data/peer-learning-club-3-work-based-learning-and-standards.xml',
        'data/peer-learning-club-4-train-the-trainers.xml',
        'data/skillman_advisory_service.xml',
        'data/webinars_catalog.xml',
        'data/skillman_technical_webinars.xml',
        'data/webinars_on_eu_fund_opportunities.xml',
        'data/peer_learning_clubs.xml',
        'data/skillman_eu_international_forum_2018.xml',
        'data/skillman_eu_international_forum_2019.xml',
        'data/tvet_digital_triathlon.xml',
        'data/skillman_at_the_european_skills_week_2020.xml',
        'data/2015_international_conference.xml',
        'data/2016_international_conference.xml',
        'data/second_international_conference.xml',
        'data/news.xml',
        'data/why.xml',
        'data/contacts.xml',
        'data/focus.xml',
        'data/partners.xml',
        'data/bmet.xml',
        'data/jlr.xml',
        'data/sas.xml',
        'data/skillnet_events.xml',
        'data/tc_5.xml',
        'data/cepas.xml',
        'data/cnr.xml',
        'data/crf.xml',
        'data/ambassadors.xml',
        'data/members_list.xml',
        'data/members.xml',
        'data/new_event.xml',
        'data/the_conference.xml',
        'data/cscs.xml',
        'data/eal.xml',
        'data/eef.xml',
        'data/iu.xml',
        'data/awards-candidatures.xml',
    ],
    # only loaded in demonstration mode
     # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/skillman_website/static/src/css/rs6.css',
            # '/skillman_website/static/src/js/rs6.js',

        ],
    }

}