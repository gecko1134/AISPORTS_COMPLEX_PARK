import sys


import os
import sys

BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from ai_modules.demand_forecasting import DemandForecaster
from ai_modules.scheduling_optimizer import optimize_schedule
from ai_modules.sponsorship_matcher import match_sponsors
from ai_modules.dynamic_contract_generator import generate_contract
from ai_modules.membership_churn import ChurnPredictor
from ai_modules.marketing_optimizer import optimize_campaign


import optimize_schedule
import match_sponsors
import generate_contract
import ChurnPredictor
import optimize_campaign
import member_selector
import auto_contract_generator
import header_loader
import fundraising_launch_center
import grant_renewal_manager
import investor_kit_generator
import board_packet_pdf_generator
import funding_narrative_sync
import crm_pipeline_dashboard
import board_report_scheduler
import hubspot_deal_logger
import sponsor_pitch_portal
import mailchimp_lead_collector
import marketing_packet_builder
import screen_rotation_scheduler
import media_display_rotator
import investor_pitch_portal
import admin_override_console
import expiring_link_manager
import sponsor_link_sender
import flipbook_pitch_creator
import sponsor_pdf_packet
import sponsor_pitchbook_builder
import sponsor_proposal_pdf
import ai_sponsor_pricing_trends
import sponsorship_inventory_limiter
import crm_grant_donor_sync
import pdf_grant_exporter
import grant_alert_center
import grant_writer_ai
import grant_match_ai
import grant_status_manager
import donation_landing_page
import crm_export_generator
import donation_checkout
import donation_campaign_viewer
import donor_match_ai
import donor_message_builder
import donor_profile_creator
import donation_goal_tracker
import portal_router
import upsell_offer_engine
import member_portal
import sponsor_portal
import public_schedule
import sponsor_map_viewer
import ai_facility_chat
import slack_alert_center
import webhook_automation
import admin_sidebar_badges
import daily_task_scheduler
import ai_voice_responder
import member_alerts_auto
import credential_expiry_alerts
import usage_alerts_auto
import contract_alerts_auto
import platform_guidebook_writer
import board_pdf_exporter
import finance_feed_connector
import board_financial_summary
import revenue_projection_simulator
import sponsorship_revenue_builder
import event_admin
import surface_usage_by_type
import governance_admin
import governance_diagram
import financial_feed_sync
import sms_alert_center
import real_time_dashboard
import gsheets_sync
import event_profit_analyzer
import adaptive_use_planner
import park_activity_dashboard
import surface_demand_heatmap
import tournament_scheduler
import international_team_portal
import esports_manager
import adaptive_sports_center
import streamlit as st
import json
import auth
import ai_event_forecast
import ai_matchmaker_tool
import ai_revenue_maximizer
import ai_scheduler_tool
import ai_scheduling_suggestions
import ai_sponsor_opportunity_finder
import ai_strategy_dashboard
import ai_suggestion_digest
import ai_voice_command
import auth
import central_dashboard
import complex_usage_optimizer
import contract_insights_ai
import contract_usage_tracker
import dome_usage_tool
import dynamic_pricing_tool
import email_notifications
import event_control_panel
import event_creator_ai
import event_types_config
import facility_access_tracker
import facility_capacity_alerts
import facility_contract_monitor
import facility_layout_map
import facility_master_tracker
import facility_membership_comparator_ai
import facility_membership_monitor
import flipbook_embedder
import google_sheets_sync
import governance_tool
import league_coordinator
import marketing_flipbook_generator
import membership_credit_tracker
import membership_crm_tracker
import membership_dashboard
import membership_goal_tracker
import membership_insights_ai
import membership_loyalty_rewards
import membership_marketing_ai
import membership_ticketing_integration
import mentorship_center
import mobile_friendly_ui
import nil_tracker
import pandadoc_contract
import pdf_export_tool
import performance_goal_ai
import proposal_to_pdf
import referee_manager
import report_download_portal
import revenue_heatmap
import revenue_proforma_auto
import scholarship_fund_manager
import scholarship_tracker
import setup_assistant_ai
import sponsor_dashboard
import sponsorship_ai_calculator
import sponsorship_availability
import sponsorship_contract_generator
import sponsorship_inventory_manager
import sponsorship_roi_tracker
import sponsorship_tracker
import sport_library
import student_committee
import team_club_manager
import trail_access_planner
import visual_calendar_layout
import volunteer_hub
import weekly_report_generator
import investor_pitch_portal
import admin_override_console




with open('users.json') as f:
    users = json.load(f)

def login():
    st.sidebar.header('🔐 Login')
    email = st.sidebar.text_input('Email')
    password = st.sidebar.text_input('Password', type='password')
    if st.sidebar.button('Login'):
        user = users.get(email)
        if user and user['password'] == password:
            st.session_state.user = {'email': email, 'role': user['role']}
        else:
            st.sidebar.error('Invalid credentials.')

def logout():
    if st.sidebar.button('Logout'):
        st.session_state.user = None

TOOLS = {
    "Ai Event Forecast": ai_event_forecast,
    "Ai Matchmaker Tool": ai_matchmaker_tool,
    "Ai Revenue Maximizer": ai_revenue_maximizer,
    "Ai Scheduler Tool": ai_scheduler_tool,
    "Ai Scheduling Suggestions": ai_scheduling_suggestions,
    "Ai Sponsor Opportunity Finder": ai_sponsor_opportunity_finder,
    "Ai Strategy Dashboard": ai_strategy_dashboard,
    "Ai Suggestion Digest": ai_suggestion_digest,
    "Ai Voice Command": ai_voice_command,
    "Auth": auth,
    "Central Dashboard": central_dashboard,
    "Complex Usage Optimizer": complex_usage_optimizer,
    "Contract Insights Ai": contract_insights_ai,
    "Contract Usage Tracker": contract_usage_tracker,
    "Dome Usage Tool": dome_usage_tool,
    "Dynamic Pricing Tool": dynamic_pricing_tool,
    "Email Notifications": email_notifications,
    "Event Control Panel": event_control_panel,
    "Event Creator Ai": event_creator_ai,
    "Event Types Config": event_types_config,
    "Facility Access Tracker": facility_access_tracker,
    "Facility Capacity Alerts": facility_capacity_alerts,
    "Facility Contract Monitor": facility_contract_monitor,
    "Facility Layout Map": facility_layout_map,
    "Facility Master Tracker": facility_master_tracker,
    "Facility Membership Comparator Ai": facility_membership_comparator_ai,
    "Facility Membership Monitor": facility_membership_monitor,
    "Flipbook Embedder": flipbook_embedder,
    "Google Sheets Sync": google_sheets_sync,
    "Governance Tool": governance_tool,
    "League Coordinator": league_coordinator,
    "Marketing Flipbook Generator": marketing_flipbook_generator,
    "Membership Credit Tracker": membership_credit_tracker,
    "Membership Crm Tracker": membership_crm_tracker,
    "Membership Dashboard": membership_dashboard,
    "Membership Goal Tracker": membership_goal_tracker,
    "Membership Insights Ai": membership_insights_ai,
    "Membership Loyalty Rewards": membership_loyalty_rewards,
    "Membership Marketing Ai": membership_marketing_ai,
    "Membership Ticketing Integration": membership_ticketing_integration,
    "Mentorship Center": mentorship_center,
    "Mobile Friendly Ui": mobile_friendly_ui,
    "Nil Tracker": nil_tracker,
    "Pandadoc Contract": pandadoc_contract,
    "Pdf Export Tool": pdf_export_tool,
    "Performance Goal Ai": performance_goal_ai,
    "Proposal To Pdf": proposal_to_pdf,
    "Referee Manager": referee_manager,
    "Report Download Portal": report_download_portal,
    "Revenue Heatmap": revenue_heatmap,
    "Revenue Proforma Auto": revenue_proforma_auto,
    "Scholarship Fund Manager": scholarship_fund_manager,
    "Scholarship Tracker": scholarship_tracker,
    "Setup Assistant Ai": setup_assistant_ai,
    "Sponsor Dashboard": sponsor_dashboard,
    "Sponsorship Ai Calculator": sponsorship_ai_calculator,
    "Sponsorship Availability": sponsorship_availability,
    "Sponsorship Contract Generator": sponsorship_contract_generator,
    "Sponsorship Inventory Manager": sponsorship_inventory_manager,
    "Sponsorship Roi Tracker": sponsorship_roi_tracker,
    "Sponsorship Tracker": sponsorship_tracker,
    "Sport Library": sport_library,
    "Student Committee": student_committee,
    "Team Club Manager": team_club_manager,
    "Trail Access Planner": trail_access_planner,
    "Visual Calendar Layout": visual_calendar_layout,
    "Volunteer Hub": volunteer_hub,
    "Weekly Report Generator": weekly_report_generator,
    "Esports Manager": esports_manager,
    "Adaptive Sports Center": adaptive_sports_center,
    "Tournament Scheduler": tournament_scheduler,
    "International Team Portal": international_team_portal,
    "Park Activity Dashboard": park_activity_dashboard,
    "Surface Demand Heatmap": surface_demand_heatmap,
    "Event Profitability Analyzer": event_profit_analyzer,
    "Adaptive Use Planner": adaptive_use_planner,
    "Real-Time Dashboard": real_time_dashboard,
    "Google Sheets Sync": gsheets_sync,
    "SMS Alert Center": sms_alert_center,
    "Event Admin": event_admin,
    "Surface Usage by Type": surface_usage_by_type,
    "Governance Admin": governance_admin,
    "Governance Diagram": governance_diagram,
    "Financial Feed Sync": financial_feed_sync,
    "Revenue Projection Simulator": revenue_projection_simulator,
    "Sponsorship Revenue Builder": sponsorship_revenue_builder,
    "Board Financial Summary": board_financial_summary,
    "Board PDF Exporter": board_pdf_exporter,
    "Finance Feed Connector": finance_feed_connector,
    "Platform Guidebook": platform_guidebook_writer,
    "Surface Gap Alerts": usage_alerts_auto,
    "Sponsor Contract Alerts": contract_alerts_auto,
    "Member Alerts Auto": member_alerts_auto,
    "Credential Expiry Alerts": credential_expiry_alerts,
    "Daily Task Scheduler": daily_task_scheduler,
    "Voice Assistant": ai_voice_responder,
    "Admin Sidebar Badges": admin_sidebar_badges,
    "Slack Alert Center": slack_alert_center,
    "Webhook Automation": webhook_automation,
    "AI Facility Chat": ai_facility_chat,
    "Public Schedule": public_schedule,
    "Sponsor Map Viewer": sponsor_map_viewer,
    "Member Portal": member_portal,
    "Sponsor Portal": sponsor_portal,
    "Portal Router": portal_router,
    "Upsell Offer Engine": upsell_offer_engine,
    "Donor Profile Creator": donor_profile_creator,
    "Donation Goal Tracker": donation_goal_tracker,
    "Donor Match AI": donor_match_ai,
    "Donor Message Builder": donor_message_builder,
    "Donation Checkout": donation_checkout,
    "Donation Campaign Viewer": donation_campaign_viewer,
    "Public Donation Page": donation_landing_page,
    "CRM Export Builder": crm_export_generator,
    "AI Grant Match": grant_match_ai,
    "Grant Status Tracker": grant_status_manager,
    "Grant Alerts": grant_alert_center,
    "AI Grant Writer": grant_writer_ai,
    "CRM Sync (Grants & Donors)": crm_grant_donor_sync,
    "PDF Grant Exporter": pdf_grant_exporter,
    "AI Sponsor Pricing Trends": ai_sponsor_pricing_trends,
    "Sponsor Inventory Limits": sponsorship_inventory_limiter,
    "AI Sponsorship Pitchbook": sponsor_pitchbook_builder,
    "Sponsor Proposal PDF": sponsor_proposal_pdf,
    "Flipbook Pitch Creator": flipbook_pitch_creator,
    "Sponsor Packet PDF": sponsor_pdf_packet,
    "Sponsor Link Generator": sponsor_link_generator,
    "Expiring Link Generator": expiring_link_manager,
    "Sponsor Link Sender": sponsor_link_sender,
    "Investor Portal": investor_pitch_portal,
    "Admin Override Console": admin_override_console,
    "Investor Portal": investor_pitch_portal,
    "Admin Override Console": admin_override_console,
    "Screen Scheduler": screen_rotation_scheduler,
    "Media Rotator": media_display_rotator,
    "Marketing Packet Builder": marketing_packet_builder,
    "Sponsor Pitch Portal": sponsor_pitch_portal,
    "Mailchimp Lead Collector": mailchimp_lead_collector,
    "HubSpot Deal Logger": hubspot_deal_logger,
    "CRM Pipeline Dashboard": crm_pipeline_dashboard,
    "Board Report Scheduler": board_report_scheduler,
    "Board Packet Generator": board_packet_pdf_generator,
    "Fundraising Narrative Sync": funding_narrative_sync,
    "Grant Renewal Tracker": grant_renewal_manager,
    "Investor Kit Generator": investor_kit_generator,
    "Fundraising Launch Center": fundraising_launch_center,
    "Membership Recommender": member_selector,
    "Contract Generator": auto_contract_generator,
}

def run():
    st.set_page_config(page_title='Venture North Admin', layout='wide')
    if 'user' not in st.session_state or not st.session_state.user:
        login()
        return
    user = st.session_state.user
    st.sidebar.success(f"Logged in as {user['email']} ({user['role']})")
    logout()
    selection = st.sidebar.selectbox('Choose a Tool', list(TOOLS.keys()))
    if selection in TOOLS:
        TOOLS[selection].run()
        header_loader.run()
        st.sidebar.title('AI Optimizations')

if st.sidebar.button('Forecast Demand'):
    st.write('Demand Forecast:')
    # TODO: load booking_data.csv and call DemandForecaster.predict()

if st.sidebar.button('Optimize Schedule'):
    st.write('Optimized Schedule:')
    # TODO: load schedule_requests.csv, resources.json, call optimize_schedule()

if st.sidebar.button('Match Sponsors'):
    st.write('Sponsor Matches:')
    # TODO: load assets.csv and sponsors.csv, call match_sponsors()

if st.sidebar.button('Generate Dynamic Contract'):
    st.write('Contract Link:')
    # TODO: call generate_contract(template_id, data, api_key) and show URL

if st.sidebar.button('Predict Churn'):
    st.write('Churn Risk Scores:')
    # TODO: load member_features.csv, call ChurnPredictor.predict()

if st.sidebar.button('Optimize Campaign'):
    st.write('Campaign Result:')
    # TODO: load invites.csv, call optimize_campaign()

st.title('SportAI Suite with AI Modules')
st.write('Select an AI tool from the sidebar to get started.')

run()
import os
import sys
import streamlit as st
import json
from typing import Dict, Any

# Add current directory to Python path
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import AI modules (with error handling)
try:
    from ai_modules.demand_forecasting import DemandForecaster
    from ai_modules.scheduling_optimizer import optimize_schedule
    from ai_modules.sponsorship_matcher import match_sponsors
    from ai_modules.dynamic_contract_generator import generate_contract
    from ai_modules.membership_churn import ChurnPredictor
    from ai_modules.marketing_optimizer import optimize_campaign
    AI_MODULES_AVAILABLE = True
except ImportError as e:
    st.warning(f"AI modules not found: {e}")
    AI_MODULES_AVAILABLE = False

# Import all other modules with error handling
def safe_import(module_name):
    """Safely import a module and return it, or None if import fails"""
    try:
        return __import__(module_name)
    except ImportError:
        return None

# Core modules
modules = {
    'auth': safe_import('auth'),
    'header_loader': safe_import('header_loader'),
    
    # AI Tools
    'ai_event_forecast': safe_import('ai_event_forecast'),
    'ai_matchmaker_tool': safe_import('ai_matchmaker_tool'),
    'ai_revenue_maximizer': safe_import('ai_revenue_maximizer'),
    'ai_scheduler_tool': safe_import('ai_scheduler_tool'),
    'ai_scheduling_suggestions': safe_import('ai_scheduling_suggestions'),
    'ai_sponsor_opportunity_finder': safe_import('ai_sponsor_opportunity_finder'),
    'ai_strategy_dashboard': safe_import('ai_strategy_dashboard'),
    'ai_suggestion_digest': safe_import('ai_suggestion_digest'),
    'ai_voice_command': safe_import('ai_voice_command'),
    'ai_facility_chat': safe_import('ai_facility_chat'),
    'ai_voice_responder': safe_import('ai_voice_responder'),
    
    # Core Management
    'central_dashboard': safe_import('central_dashboard'),
    'event_control_panel': safe_import('event_control_panel'),
    'event_creator_ai': safe_import('event_creator_ai'),
    'facility_master_tracker': safe_import('facility_master_tracker'),
    'membership_dashboard': safe_import('membership_dashboard'),
    
    # Facility Management
    'facility_access_tracker': safe_import('facility_access_tracker'),
    'facility_capacity_alerts': safe_import('facility_capacity_alerts'),
    'facility_contract_monitor': safe_import('facility_contract_monitor'),
    'facility_layout_map': safe_import('facility_layout_map'),
    'facility_membership_monitor': safe_import('facility_membership_monitor'),
    'complex_usage_optimizer': safe_import('complex_usage_optimizer'),
    'dome_usage_tool': safe_import('dome_usage_tool'),
    'surface_usage_by_type': safe_import('surface_usage_by_type'),
    'surface_demand_heatmap': safe_import('surface_demand_heatmap'),
    'adaptive_use_planner': safe_import('adaptive_use_planner'),
    
    # Membership & CRM
    'membership_credit_tracker': safe_import('membership_credit_tracker'),
    'membership_crm_tracker': safe_import('membership_crm_tracker'),
    'membership_goal_tracker': safe_import('membership_goal_tracker'),
    'membership_insights_ai': safe_import('membership_insights_ai'),
    'membership_loyalty_rewards': safe_import('membership_loyalty_rewards'),
    'membership_marketing_ai': safe_import('membership_marketing_ai'),
    'member_portal': safe_import('member_portal'),
    'member_selector': safe_import('member_selector'),
    
    # Sponsorship & Revenue
    'sponsor_dashboard': safe_import('sponsor_dashboard'),
    'sponsorship_ai_calculator': safe_import('sponsorship_ai_calculator'),
    'sponsorship_availability': safe_import('sponsorship_availability'),
    'sponsorship_contract_generator': safe_import('sponsorship_contract_generator'),
    'sponsorship_inventory_manager': safe_import('sponsorship_inventory_manager'),
    'sponsorship_roi_tracker': safe_import('sponsorship_roi_tracker'),
    'sponsorship_tracker': safe_import('sponsorship_tracker'),
    'sponsor_portal': safe_import('sponsor_portal'),
    'revenue_heatmap': safe_import('revenue_heatmap'),
    'revenue_projection_simulator': safe_import('revenue_projection_simulator'),
    'sponsorship_revenue_builder': safe_import('sponsorship_revenue_builder'),
    'ai_sponsor_pricing_trends': safe_import('ai_sponsor_pricing_trends'),
    'sponsor_pitch_portal': safe_import('sponsor_pitch_portal'),
    'sponsor_pitchbook_builder': safe_import('sponsor_pitchbook_builder'),
    'sponsor_pdf_packet': safe_import('sponsor_pdf_packet'),
    'sponsor_link_sender': safe_import('sponsor_link_sender'),
    'sponsor_map_viewer': safe_import('sponsor_map_viewer'),
    
    # Events & Sports
    'tournament_scheduler': safe_import('tournament_scheduler'),
    'esports_manager': safe_import('esports_manager'),
    'adaptive_sports_center': safe_import('adaptive_sports_center'),
    'league_coordinator': safe_import('league_coordinator'),
    'team_club_manager': safe_import('team_club_manager'),
    'sport_library': safe_import('sport_library'),
    'event_profit_analyzer': safe_import('event_profit_analyzer'),
    'event_admin': safe_import('event_admin'),
    'international_team_portal': safe_import('international_team_portal'),
    'park_activity_dashboard': safe_import('park_activity_dashboard'),
    
    # Financial & Reporting
    'board_pdf_exporter': safe_import('board_pdf_exporter'),
    'finance_feed_connector': safe_import('finance_feed_connector'),
    'financial_feed_sync': safe_import('financial_feed_sync'),
    'revenue_proforma_auto': safe_import('revenue_proforma_auto'),
    'weekly_report_generator': safe_import('weekly_report_generator'),
    'report_download_portal': safe_import('report_download_portal'),
    'board_packet_pdf_generator': safe_import('board_packet_pdf_generator'),
    'board_report_scheduler': safe_import('board_report_scheduler'),
    'pdf_export_tool': safe_import('pdf_export_tool'),
    
    # Grants & Fundraising
    'grant_renewal_manager': safe_import('grant_renewal_manager'),
    'grant_alert_center': safe_import('grant_alert_center'),
    'grant_writer_ai': safe_import('grant_writer_ai'),
    'grant_match_ai': safe_import('grant_match_ai'),
    'grant_status_manager': safe_import('grant_status_manager'),
    'pdf_grant_exporter': safe_import('pdf_grant_exporter'),
    'investor_kit_generator': safe_import('investor_kit_generator'),
    'investor_pitch_portal': safe_import('investor_pitch_portal'),
    'funding_narrative_sync': safe_import('funding_narrative_sync'),
    
    # Donations
    'donation_landing_page': safe_import('donation_landing_page'),
    'donation_checkout': safe_import('donation_checkout'),
    'donation_campaign_viewer': safe_import('donation_campaign_viewer'),
    'donation_goal_tracker': safe_import('donation_goal_tracker'),
    'donor_profile_creator': safe_import('donor_profile_creator'),
    'crm_export_generator': safe_import('crm_export_generator'),
    'crm_grant_donor_sync': safe_import('crm_grant_donor_sync'),
    
    # Communications & Alerts
    'email_notifications': safe_import('email_notifications'),
    'sms_alert_center': safe_import('sms_alert_center'),
    'slack_alert_center': safe_import('slack_alert_center'),
    'member_alerts_auto': safe_import('member_alerts_auto'),
    'usage_alerts_auto': safe_import('usage_alerts_auto'),
    'contract_alerts_auto': safe_import('contract_alerts_auto'),
    'credential_expiry_alerts': safe_import('credential_expiry_alerts'),
    'daily_task_scheduler': safe_import('daily_task_scheduler'),
    
    # Integrations & Tools
    'google_sheets_sync': safe_import('google_sheets_sync'),
    'gsheets_sync': safe_import('gsheets_sync'),
    'webhook_automation': safe_import('webhook_automation'),
    'pandadoc_contract': safe_import('pandadoc_contract'),
    'auto_contract_generator': safe_import('auto_contract_generator'),
    'hubspot_deal_logger': safe_import('hubspot_deal_logger'),
    'mailchimp_lead_collector': safe_import('mailchimp_lead_collector'),
    
    # Marketing & Media
    'marketing_flipbook_generator': safe_import('marketing_flipbook_generator'),
    'marketing_packet_builder': safe_import('marketing_packet_builder'),
    'flipbook_embedder': safe_import('flipbook_embedder'),
    'flipbook_pitch_creator': safe_import('flipbook_pitch_creator'),
    'screen_rotation_scheduler': safe_import('screen_rotation_scheduler'),
    'media_display_rotator': safe_import('media_display_rotator'),
    
    # Governance & Admin
    'governance_admin': safe_import('governance_admin'),
    'governance_diagram': safe_import('governance_diagram'),
    'governance_tool': safe_import('governance_tool'),
    'admin_override_console': safe_import('admin_override_console'),
    'admin_sidebar_badges': safe_import('admin_sidebar_badges'),
    'platform_guidebook_writer': safe_import('platform_guidebook_writer'),
    
    # Utilities
    'dynamic_pricing_tool': safe_import('dynamic_pricing_tool'),
    'visual_calendar_layout': safe_import('visual_calendar_layout'),
    'mobile_friendly_ui': safe_import('mobile_friendly_ui'),
    'real_time_dashboard': safe_import('real_time_dashboard'),
    'setup_assistant_ai': safe_import('setup_assistant_ai'),
    'portal_router': safe_import('portal_router'),
    'upsell_offer_engine': safe_import('upsell_offer_engine'),
    'public_schedule': safe_import('public_schedule'),
    'expiring_link_manager': safe_import('expiring_link_manager'),
    
    # Specialty Programs
    'scholarship_fund_manager': safe_import('scholarship_fund_manager'),
    'scholarship_tracker': safe_import('scholarship_tracker'),
    'mentorship_center': safe_import('mentorship_center'),
    'volunteer_hub': safe_import('volunteer_hub'),
    'student_committee': safe_import('student_committee'),
    'referee_manager': safe_import('referee_manager'),
    'nil_tracker': safe_import('nil_tracker'),
    'trail_access_planner': safe_import('trail_access_planner'),
    
    # Contract & Performance
    'contract_insights_ai': safe_import('contract_insights_ai'),
    'contract_usage_tracker': safe_import('contract_usage_tracker'),
    'performance_goal_ai': safe_import('performance_goal_ai'),
    'facility_membership_comparator_ai': safe_import('facility_membership_comparator_ai'),
    'membership_ticketing_integration': safe_import('membership_ticketing_integration'),
    'sponsorship_inventory_limiter': safe_import('sponsorship_inventory_limiter'),
}

# Filter out None values (failed imports)
available_modules = {k: v for k, v in modules.items() if v is not None}

class SportAIApp:
    def __init__(self):
        self.users = self.load_users()
        self.tools = self.build_tools_menu()
    
    def load_users(self) -> Dict[str, Any]:
        """Load user data with error handling"""
        try:
            with open('users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Create default users if file doesn't exist
            default_users = {
                "admin@sportai.com": {"password": "admin123", "role": "admin"},
                "manager@sportai.com": {"password": "manager123", "role": "manager"},
                "user@sportai.com": {"password": "user123", "role": "user"}
            }
            try:
                with open('users.json', 'w') as f:
                    json.dump(default_users, f, indent=2)
                return default_users
            except Exception:
                return default_users
        except Exception as e:
            st.error(f"Error loading users: {e}")
            return {}
    
    def build_tools_menu(self) -> Dict[str, Any]:
        """Build the tools menu from available modules"""
        tools = {}
        
        # AI Tools Category
        ai_tools = {
            "🤖 AI Event Forecast": available_modules.get('ai_event_forecast'),
            "🤖 AI Matchmaker": available_modules.get('ai_matchmaker_tool'),
            "🤖 AI Revenue Maximizer": available_modules.get('ai_revenue_maximizer'),
            "🤖 AI Scheduler": available_modules.get('ai_scheduler_tool'),
            "🤖 AI Scheduling Suggestions": available_modules.get('ai_scheduling_suggestions'),
            "🤖 AI Sponsor Finder": available_modules.get('ai_sponsor_opportunity_finder'),
            "🤖 AI Strategy Dashboard": available_modules.get('ai_strategy_dashboard'),
            "🤖 AI Suggestion Digest": available_modules.get('ai_suggestion_digest'),
            "🤖 AI Voice Command": available_modules.get('ai_voice_command'),
            "🤖 AI Facility Chat": available_modules.get('ai_facility_chat'),
            "🤖 AI Voice Assistant": available_modules.get('ai_voice_responder'),
            "🤖 AI Sponsor Pricing": available_modules.get('ai_sponsor_pricing_trends'),
            "🤖 AI Grant Writer": available_modules.get('grant_writer_ai'),
            "🤖 AI Grant Match": available_modules.get('grant_match_ai'),
        }
        
        # Core Management
        core_tools = {
            "📊 Central Dashboard": available_modules.get('central_dashboard'),
            "🎯 Event Control Panel": available_modules.get('event_control_panel'),
            "🎨 Event Creator AI": available_modules.get('event_creator_ai'),
            "🏟️ Facility Master Tracker": available_modules.get('facility_master_tracker'),
            "👥 Membership Dashboard": available_modules.get('membership_dashboard'),
            "💰 Sponsor Dashboard": available_modules.get('sponsor_dashboard'),
            "⚡ Real-Time Dashboard": available_modules.get('real_time_dashboard'),
            "🛠️ Setup Assistant AI": available_modules.get('setup_assistant_ai'),
        }
        
        # Facility Management
        facility_tools = {
            "🚪 Facility Access Tracker": available_modules.get('facility_access_tracker'),
            "⚠️ Facility Capacity Alerts": available_modules.get('facility_capacity_alerts'),
            "📋 Facility Contract Monitor": available_modules.get('facility_contract_monitor'),
            "🗺️ Facility Layout Map": available_modules.get('facility_layout_map'),
            "👥 Facility Membership Monitor": available_modules.get('facility_membership_monitor'),
            "🔧 Complex Usage Optimizer": available_modules.get('complex_usage_optimizer'),
            "🏛️ Dome Usage Tool": available_modules.get('dome_usage_tool'),
            "📊 Surface Usage by Type": available_modules.get('surface_usage_by_type'),
            "🔥 Surface Demand Heatmap": available_modules.get('surface_demand_heatmap'),
            "📈 Adaptive Use Planner": available_modules.get('adaptive_use_planner'),
            "🔍 Facility Membership Comparator": available_modules.get('facility_membership_comparator_ai'),
        }
        
        # Membership & CRM
        membership_tools = {
            "💳 Membership Credit Tracker": available_modules.get('membership_credit_tracker'),
            "👥 Membership CRM Tracker": available_modules.get('membership_crm_tracker'),
            "🎯 Membership Goal Tracker": available_modules.get('membership_goal_tracker'),
            "📊 Membership Insights AI": available_modules.get('membership_insights_ai'),
            "🏆 Membership Loyalty Rewards": available_modules.get('membership_loyalty_rewards'),
            "📢 Membership Marketing AI": available_modules.get('membership_marketing_ai'),
            "🔗 Membership Ticketing Integration": available_modules.get('membership_ticketing_integration'),
            "🚪 Member Portal": available_modules.get('member_portal'),
            "🎯 Member Selector": available_modules.get('member_selector'),
        }
        
        # Sponsorship & Revenue
        sponsorship_tools = {
            "🤝 Sponsorship AI Calculator": available_modules.get('sponsorship_ai_calculator'),
            "📅 Sponsorship Availability": available_modules.get('sponsorship_availability'),
            "📄 Sponsorship Contract Generator": available_modules.get('sponsorship_contract_generator'),
            "📦 Sponsorship Inventory Manager": available_modules.get('sponsorship_inventory_manager'),
            "📈 Sponsorship ROI Tracker": available_modules.get('sponsorship_roi_tracker'),
            "📊 Sponsorship Tracker": available_modules.get('sponsorship_tracker'),
            "🚪 Sponsor Portal": available_modules.get('sponsor_portal'),
            "💰 Sponsorship Revenue Builder": available_modules.get('sponsorship_revenue_builder'),
            "🎯 Sponsor Pitch Portal": available_modules.get('sponsor_pitch_portal'),
            "📖 Sponsor Pitchbook Builder": available_modules.get('sponsor_pitchbook_builder'),
            "📄 Sponsor PDF Packet": available_modules.get('sponsor_pdf_packet'),
            "🔗 Sponsor Link Sender": available_modules.get('sponsor_link_sender'),
            "🗺️ Sponsor Map Viewer": available_modules.get('sponsor_map_viewer'),
            "📊 Sponsorship Inventory Limiter": available_modules.get('sponsorship_inventory_limiter'),
        }
        
        # Revenue & Financial
        financial_tools = {
            "🔥 Revenue Heatmap": available_modules.get('revenue_heatmap'),
            "📈 Revenue Projection Simulator": available_modules.get('revenue_projection_simulator'),
            "📊 Revenue Proforma Auto": available_modules.get('revenue_proforma_auto'),
            "💰 Dynamic Pricing Tool": available_modules.get('dynamic_pricing_tool'),
            "💼 Finance Feed Connector": available_modules.get('finance_feed_connector'),
            "🔄 Financial Feed Sync": available_modules.get('financial_feed_sync'),
        }
        
        # Sports & Events
        sports_tools = {
            "🏆 Tournament Scheduler": available_modules.get('tournament_scheduler'),
            "🎮 Esports Manager": available_modules.get('esports_manager'),
            "♿ Adaptive Sports Center": available_modules.get('adaptive_sports_center'),
            "🏟️ League Coordinator": available_modules.get('league_coordinator'),
            "👥 Team Club Manager": available_modules.get('team_club_manager'),
            "📚 Sport Library": available_modules.get('sport_library'),
            "💰 Event Profit Analyzer": available_modules.get('event_profit_analyzer'),
            "🎯 Event Admin": available_modules.get('event_admin'),
            "🌍 International Team Portal": available_modules.get('international_team_portal'),
            "🏞️ Park Activity Dashboard": available_modules.get('park_activity_dashboard'),
        }
        
        # Reporting & Documents
        reporting_tools = {
            "📋 Board PDF Exporter": available_modules.get('board_pdf_exporter'),
            "📊 Board Packet Generator": available_modules.get('board_packet_pdf_generator'),
            "📅 Board Report Scheduler": available_modules.get('board_report_scheduler'),
            "📄 Weekly Report Generator": available_modules.get('weekly_report_generator'),
            "📥 Report Download Portal": available_modules.get('report_download_portal'),
            "📄 PDF Export Tool": available_modules.get('pdf_export_tool'),
            "📚 Platform Guidebook": available_modules.get('platform_guidebook_writer'),
        }
        
        # Grants & Fundraising
        grants_tools = {
            "🔄 Grant Renewal Manager": available_modules.get('grant_renewal_manager'),
            "⚠️ Grant Alerts": available_modules.get('grant_alert_center'),
            "📊 Grant Status Tracker": available_modules.get('grant_status_manager'),
            "📄 PDF Grant Exporter": available_modules.get('pdf_grant_exporter'),
            "💼 Investor Kit Generator": available_modules.get('investor_kit_generator'),
            "🎯 Investor Portal": available_modules.get('investor_pitch_portal'),
            "📝 Funding Narrative Sync": available_modules.get('funding_narrative_sync'),
            "💰 Donation Landing Page": available_modules.get('donation_landing_page'),
            "🛒 Donation Checkout": available_modules.get('donation_checkout'),
            "📊 Donation Campaign Viewer": available_modules.get('donation_campaign_viewer'),
            "🎯 Donation Goal Tracker": available_modules.get('donation_goal_tracker'),
            "👤 Donor Profile Creator": available_modules.get('donor_profile_creator'),
        }
        
        # Communications & Marketing
        communication_tools = {
            "📧 Email Notifications": available_modules.get('email_notifications'),
            "📱 SMS Alert Center": available_modules.get('sms_alert_center'),
            "💬 Slack Alert Center": available_modules.get('slack_alert_center'),
            "⚠️ Member Alerts Auto": available_modules.get('member_alerts_auto'),
            "📊 Usage Alerts Auto": available_modules.get('usage_alerts_auto'),
            "📋 Contract Alerts Auto": available_modules.get('contract_alerts_auto'),
            "🔐 Credential Expiry Alerts": available_modules.get('credential_expiry_alerts'),
            "📅 Daily Task Scheduler": available_modules.get('daily_task_scheduler'),
            "📦 Marketing Packet Builder": available_modules.get('marketing_packet_builder'),
            "📖 Marketing Flipbook Generator": available_modules.get('marketing_flipbook_generator'),
            "📚 Flipbook Embedder": available_modules.get('flipbook_embedder'),
            "🎨 Flipbook Pitch Creator": available_modules.get('flipbook_pitch_creator'),
            "🔄 Screen Rotation Scheduler": available_modules.get('screen_rotation_scheduler'),
            "📺 Media Display Rotator": available_modules.get('media_display_rotator'),
        }
        
        # Integrations & Sync
        integration_tools = {
            "📊 Google Sheets Sync": available_modules.get('google_sheets_sync'),
            "🔄 GSheets Sync": available_modules.get('gsheets_sync'),
            "🔗 Webhook Automation": available_modules.get('webhook_automation'),
            "📄 PandaDoc Contract": available_modules.get('pandadoc_contract'),
            "🤖 Auto Contract Generator": available_modules.get('auto_contract_generator'),
            "🔄 HubSpot Deal Logger": available_modules.get('hubspot_deal_logger'),
            "📧 Mailchimp Lead Collector": available_modules.get('mailchimp_lead_collector'),
            "📊 CRM Export Generator": available_modules.get('crm_export_generator'),
            "🔄 CRM Grant Donor Sync": available_modules.get('crm_grant_donor_sync'),
        }
        
        # Specialty & Admin
        specialty_tools = {
            "🎓 Scholarship Fund Manager": available_modules.get('scholarship_fund_manager'),
            "📊 Scholarship Tracker": available_modules.get('scholarship_tracker'),
            "👨‍🏫 Mentorship Center": available_modules.get('mentorship_center'),
            "🤝 Volunteer Hub": available_modules.get('volunteer_hub'),
            "🎓 Student Committee": available_modules.get('student_committee'),
            "👔 Referee Manager": available_modules.get('referee_manager'),
            "📊 NIL Tracker": available_modules.get('nil_tracker'),
            "🥾 Trail Access Planner": available_modules.get('trail_access_planner'),
            "🔧 Admin Override Console": available_modules.get('admin_override_console'),
            "🏷️ Admin Sidebar Badges": available_modules.get('admin_sidebar_badges'),
            "🔗 Portal Router": available_modules.get('portal_router'),
            "💎 Upsell Offer Engine": available_modules.get('upsell_offer_engine'),
            "📅 Public Schedule": available_modules.get('public_schedule'),
            "⏰ Expiring Link Manager": available_modules.get('expiring_link_manager'),
        }
        
        # Utilities & Tools
        utility_tools = {
            "📱 Mobile Friendly UI": available_modules.get('mobile_friendly_ui'),
            "📅 Visual Calendar Layout": available_modules.get('visual_calendar_layout'),
            "📊 Contract Insights AI": available_modules.get('contract_insights_ai'),
            "📋 Contract Usage Tracker": available_modules.get('contract_usage_tracker'),
            "🎯 Performance Goal AI": available_modules.get('performance_goal_ai'),
            "🏛️ Governance Tool": available_modules.get('governance_tool'),
            "📊 Governance Admin": available_modules.get('governance_admin'),
            "📈 Governance Diagram": available_modules.get('governance_diagram'),
        }
        
        # Combine all categories, filtering out None values
        all_categories = [
            ("🤖 AI Tools", ai_tools),
            ("📊 Core Management", core_tools),
            ("🏟️ Facility Management", facility_tools),
            ("👥 Membership & CRM", membership_tools),
            ("🤝 Sponsorship & Revenue", sponsorship_tools),
            ("💰 Financial Tools", financial_tools),
            ("🏆 Sports & Events", sports_tools),
            ("📋 Reporting & Documents", reporting_tools),
            ("💰 Grants & Fundraising", grants_tools),
            ("📢 Communications & Marketing", communication_tools),
            ("🔄 Integrations & Sync", integration_tools),
            ("🎯 Specialty & Admin", specialty_tools),
            ("🛠️ Utilities & Tools", utility_tools),
        ]
        
        for category_name, category_tools in all_categories:
            available_tools = {k: v for k, v in category_tools.items() if v is not None}
            tools.update(available_tools)
        
        return tools
    
    def login(self):
        """Handle user login"""
        st.sidebar.header('🔐 Login')
        email = st.sidebar.text_input('Email', key='login_email')
        password = st.sidebar.text_input('Password', type='password', key='login_password')
        
        if st.sidebar.button('Login'):
            user = self.users.get(email)
            if user and user['password'] == password:
                st.session_state.user = {'email': email, 'role': user['role']}
                st.sidebar.success('Login successful!')
                st.rerun()
            else:
                st.sidebar.error('Invalid credentials.')
        
        # Show available demo accounts
        with st.sidebar.expander("📝 Demo Accounts"):
            st.write("**Admin:** admin@sportai.com / admin123")
            st.write("**Manager:** manager@sportai.com / manager123")
            st.write("**User:** user@sportai.com / user123")
    
    def logout(self):
        """Handle user logout"""
        if st.sidebar.button('🚪 Logout'):
            st.session_state.user = None
            st.rerun()
    
    def render_ai_sidebar(self):
        """Render the AI optimization sidebar"""
        if not AI_MODULES_AVAILABLE:
            st.sidebar.warning("⚠️ AI modules not available")
            return
            
        st.sidebar.markdown("---")
        st.sidebar.title('🤖 AI Optimizations')
        
        if st.sidebar.button('📈 Forecast Demand'):
            try:
                forecaster = DemandForecaster()
                st.success("✅ Demand forecasting initiated!")
                st.info("💡 Next: Load booking_data.csv and call DemandForecaster.predict()")
            except Exception as e:
                st.error(f"❌ Error in demand forecasting: {e}")
        
        if st.sidebar.button('📅 Optimize Schedule'):
            try:
                st.success("✅ Schedule optimization initiated!")
                st.info("💡 Next: Load schedule_requests.csv and resources.json")
            except Exception as e:
                st.error(f"❌ Error in schedule optimization: {e}")
        
        if st.sidebar.button('🤝 Match Sponsors'):
            try:
                st.success("✅ Sponsor matching initiated!")
                st.info("💡 Next: Load assets.csv and sponsors.csv")
            except Exception as e:
                st.error(f"❌ Error in sponsor matching: {e}")
        
        if st.sidebar.button('📄 Generate Contract'):
            try:
                st.success("✅ Dynamic contract generation initiated!")
                st.info("💡 Next: Call generate_contract(template_id, data, api_key)")
            except Exception as e:
                st.error(f"❌ Error in contract generation: {e}")
        
        if st.sidebar.button('⚠️ Predict Churn'):
            try:
                predictor = ChurnPredictor()
                st.success("✅ Churn prediction initiated!")
                st.info("💡 Next: Load member_features.csv")
            except Exception as e:
                st.error(f"❌ Error in churn prediction: {e}")
        
        if st.sidebar.button('📢 Optimize Campaign'):
            try:
                st.success("✅ Campaign optimization initiated!")
                st.info("💡 Next: Load invites.csv")
            except Exception as e:
                st.error(f"❌ Error in campaign optimization: {e}")
    
    def run(self):
        """Main application runner"""
        st.set_page_config(
            page_title='SportAI Suite - Venture North Admin',
            page_icon='🏟️',
            layout='wide',
            initial_sidebar_state='expanded'
        )
        
        # Check if user is logged in
        if 'user' not in st.session_state or not st.session_state.user:
            st.title('🏟️ SportAI Suite')
            st.markdown("""
            ### Welcome to the Comprehensive Sports Facility Management Platform
            
            SportAI Suite is your all-in-one solution for managing sports facilities, memberships, 
            sponsorships, events, and revenue optimization with cutting-edge AI technology.
            
            **Key Features:**
            - 🤖 AI-powered demand forecasting and scheduling optimization
            - 🏟️ Complete facility and membership management
            - 💰 Revenue optimization and sponsorship matching
            - 📊 Real-time analytics and reporting
            - 🎯 Event management and tournament scheduling
            - 📱 Mobile-friendly interface with multi-user support
            
            **Please log in using the sidebar to access all tools.**
            """)
            
            # Show quick stats
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Available Tools", len(self.tools))
            with col2:
                st.metric("AI Modules", "✅ Ready" if AI_MODULES_AVAILABLE else "❌ Not Available")
            with col3:
                st.metric("Module Categories", "13")
            
            self.login()
            return
        
        # User is logged in
        user = st.session_state.user
        st.sidebar.success(f"✅ Logged in as {user['email']} ({user['role'].title()})")
        self.logout()
        
        # Tool selection
        st.sidebar.markdown("---")
        st.sidebar.title('🧭 Select Tool')
        
        if not self.tools:
            st.sidebar.warning("⚠️ No tools available")
            st.title('🏟️ SportAI Suite')
            st.error('❌ No modules were successfully imported. Please check your installation.')
            st.markdown("""
            ### Troubleshooting Steps:
            1. Ensure all module files are in the correct directory
            2. Check that each module has a `run()` function
            3. Verify Python path configuration
            4. Review error logs for specific import issues
            """)
            return
        
        # Create searchable tool selection
        search_term = st.sidebar.text_input("🔍 Search Tools", placeholder="Type to filter tools...")
        
        # Filter tools based on search
        if search_term:
            filtered_tools = {k: v for k, v in self.tools.items() 
                            if search_term.lower() in k.lower()}
        else:
            filtered_tools = self.tools
        
        if not filtered_tools:
            st.sidebar.warning(f"No tools found matching '{search_term}'")
            filtered_tools = self.tools
        
        selection = st.sidebar.selectbox(
            'Choose a Tool',
            list(filtered_tools.keys()),
            key='tool_selection'
        )
        
        # Quick access buttons for popular tools
        st.sidebar.markdown("### 🚀 Quick Access")
        quick_tools = [
            "📊 Central Dashboard",
            "🤖 AI Strategy Dashboard", 
            "🏟️ Facility Master Tracker",
            "👥 Membership Dashboard",
            "💰 Sponsor Dashboard"
        ]
        
        for tool in quick_tools:
            if tool in self.tools:
                if st.sidebar.button(tool.split(" ", 1)[1], key=f"quick_{tool}"):
                    st.session_state.tool_selection = tool
                    st.rerun()
        
        # Render AI sidebar
        self.render_ai_sidebar()
        
        # Run selected tool
        if selection and selection in self.tools:
            tool_module = self.tools[selection]
            if tool_module and hasattr(tool_module, 'run'):
                try:
                    # Load header if available
                    if available_modules.get('header_loader'):
                        available_modules['header_loader'].run()
                    
                    # Show current tool info
                    st.info(f"🔧 Running: {selection}")
                    
                    # Run the selected tool
                    tool_module.run()
                    
                except Exception as e:
                    st.error(f"❌ Error running {selection}: {e}")
                    st.markdown("""
                    ### Troubleshooting:
                    - Check that the module is properly implemented
                    - Verify all required dependencies are installed
                    - Review the module's `run()` function for errors
                    """)
                    
                    # Show debug info for admins
                    if user['role'] == 'admin':
                        with st.expander("🔍 Debug Information"):
                            st.code(f"Module: {tool_module}")
                            st.code(f"Error: {str(e)}")
            else:
                st.error(f"❌ Tool '{selection}' is not properly configured.")
                st.write("The selected tool does not have a valid `run()` method.")
        else:
            # Main dashboard when no specific tool is selected
            st.title('🏟️ SportAI Suite with AI Modules')
            st.markdown(f"Welcome back, **{user['email']}**! Select an AI tool from the sidebar to get started.")
            
            # Show system status
            st.markdown("## 📊 System Status")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Available Tools", len(self.tools), delta=f"+{len(available_modules)} modules")
            
            with col2:
                status = "✅ Ready" if AI_MODULES_AVAILABLE else "❌ Not Available"
                st.metric("AI Modules", status)
            
            with col3:
                st.metric("User Role", user['role'].title())
            
            with col4:
                st.metric("Session Status", "🟢 Active")
            
            # Tool categories overview
            st.markdown("## 🛠️ Available Tool Categories")
            
            # Group tools by category
            categories = {
                "🤖 AI Tools": [k for k in self.tools.keys() if k.startswith("🤖")],
                "📊 Management": [k for k in self.tools.keys() if k.startswith(("📊", "🎯", "🏟️", "👥", "💰"))],
                "🏆 Sports & Events": [k for k in self.tools.keys() if k.startswith(("🏆", "🎮", "♿", "🌍"))],
                "💰 Financial": [k for k in self.tools.keys() if k.startswith(("💰", "🔥", "📈", "💼"))],
                "📋 Reporting": [k for k in self.tools.keys() if k.startswith(("📋", "📄", "📊"))],
                "📢 Communications": [k for k in self.tools.keys() if k.startswith(("📧", "📱", "💬", "⚠️"))],
                "🔄 Integrations": [k for k in self.tools.keys() if k.startswith(("🔄", "🔗", "📊"))],
                "🛠️ Utilities": [k for k in self.tools.keys() if not any(k.startswith(prefix) for prefix in 
                    ["🤖", "📊", "🎯", "🏟️", "👥", "💰", "🏆", "🎮", "♿", "🌍", "🔥", "📈", "💼", 
                     "📋", "📄", "📧", "📱", "💬", "⚠️", "🔄", "🔗"])]
            }
            
            # Display categories in columns
            cols = st.columns(2)
            for i, (category, tools) in enumerate(categories.items()):
                if tools:  # Only show categories with tools
                    with cols[i % 2]:
                        st.markdown(f"### {category}")
                        st.markdown(f"**{len(tools)} tools available**")
                        
                        # Show first 3 tools as examples
                        for tool in tools[:3]:
                            st.markdown(f"• {tool}")
                        
                        if len(tools) > 3:
                            st.markdown(f"• ... and {len(tools) - 3} more")
                        
                        st.markdown("---")
            
            # Recent activity or quick actions
            st.markdown("## 🚀 Quick Actions")
            
            action_cols = st.columns(3)
            
            with action_cols[0]:
                if st.button("📊 Open Central Dashboard", key="dashboard_btn"):
                    if "📊 Central Dashboard" in self.tools:
                        st.session_state.tool_selection = "📊 Central Dashboard"
                        st.rerun()
            
            with action_cols[1]:
                if st.button("🤖 AI Strategy Dashboard", key="ai_dashboard_btn"):
                    if "🤖 AI Strategy Dashboard" in self.tools:
                        st.session_state.tool_selection = "🤖 AI Strategy Dashboard"
                        st.rerun()
            
            with action_cols[2]:
                if st.button("🏟️ Facility Overview", key="facility_btn"):
                    if "🏟️ Facility Master Tracker" in self.tools:
                        st.session_state.tool_selection = "🏟️ Facility Master Tracker"
                        st.rerun()
            
            # Show helpful tips
            st.markdown("## 💡 Tips")
            tips = [
                "Use the search box in the sidebar to quickly find specific tools",
                "AI optimization buttons are available in the sidebar for quick access",
                "Admin users have access to debug information when tools encounter errors",
                "All tools are organized by category with emoji indicators for easy identification"
            ]
            
            for tip in tips:
                st.markdown(f"• {tip}")

# Run the application
if __name__ == "__main__":
    app = SportAIApp()
    app.run()
