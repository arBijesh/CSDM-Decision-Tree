import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="CubeSimple CSDM Classifier", page_icon="🧊", layout="wide")

# --- STYLES (Based on your Framework Colors) ---
st.markdown("""
<style>
    /* Blue - Strategy/Design */
    .design { border-left: 6px solid #00B5AD; background-color: #F0FBFC; padding: 15px; }
    /* Orange - Technical/Manage */
    .manage { border-left: 6px solid #F2711C; background-color: #FEF6F1; padding: 15px; }
    /* Green - Service Consumption */
    .consume { border-left: 6px solid #21BA45; background-color: #F0FDF4; padding: 15px; }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
def navigate(next_step):
    st.session_state.step = next_step
    st.rerun()

def restart():
    st.session_state.step = 'start'
    st.rerun()

if 'step' not in st.session_state:
    st.session_state.step = 'start'

# --- MAIN APP ---
st.title("🧊 CubeSimple CSDM Classifier")
st.caption("Strictly aligned to CSDM Framework & Decision Tree")
st.divider()

step = st.session_state.step

# ---------------------------------------------------------
# STEP 1: BUSINESS CAPABILITY CHECK (Q1 from Diagram)
# ---------------------------------------------------------
if step == 'start':
    st.subheader("Q1: Business Capability Check")
    st.markdown("### Is this a high-level business 'Ability' or 'Function'?")
    st.info("Does it exist even without IT? (e.g., Recruiting, Payroll)")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (It's a Capability)"): navigate('res_bus_cap')
    if c2.button("NO"): navigate('check_portfolio')

# ---------------------------------------------------------
# STEP 2: SERVICE PORTFOLIO CHECK (Q2 from Diagram)
# ---------------------------------------------------------
elif step == 'check_portfolio':
    st.subheader("Q2: Service Portfolio Check")
    st.markdown("### Is this just a 'Category' or 'Folder' that holds other services?")
    st.warning("You cannot 'order' this directly. It groups other services.")
    st.markdown("**Example from Framework:** *'Service Portfolio Digital Sales Enablement'*")

    c1, c2 = st.columns(2)
    if c1.button("YES (It's a Portfolio)"): navigate('res_svc_port')
    if c2.button("NO"): navigate('check_software')

# ---------------------------------------------------------
# STEP 3: BUSINESS APPLICATION CHECK (Q3 from Diagram)
# ---------------------------------------------------------
elif step == 'check_software':
    st.subheader("Q3: Business Application Check")
    st.markdown("### Is this a named Software Product we buy and track?")
    st.info("The 'Brand Name' in our inventory.")
    st.markdown("**Example from Framework:** *'Business Application Client CRM'*")

    c1, c2 = st.columns(2)
    if c1.button("YES (It's a Business App)"): navigate('res_bus_app')
    if c2.button("NO"): navigate('check_app_service')

# ---------------------------------------------------------
# STEP 4: APPLICATION SERVICE CHECK (Q4 from Diagram)
# ---------------------------------------------------------
elif step == 'check_app_service':
    st.subheader("Q4: Application Service Check")
    st.markdown("### Is this a specific RUNNING login page or environment?")
    st.warning("The thing that actually breaks.")
    st.markdown("**Example from Framework:** *'Service Instance PROD - Client CRM'*")

    c1, c2 = st.columns(2)
    if c1.button("YES (It's an App Service)"): navigate('res_app_svc')
    if c2.button("NO"): navigate('check_business_service')

# ---------------------------------------------------------
# STEP 5: BUSINESS SERVICE CHECK (Q5 from Diagram)
# ---------------------------------------------------------
elif step == 'check_business_service':
    st.subheader("Q5: Business Service Check")
    st.markdown("### Is this 'Help' or an 'Action' a user requests to do their job?")
    st.info("Something found in the Service Catalog.")
    st.markdown("**Example from Framework:** *'Business Service Customer Lead Management'*")

    c1, c2 = st.columns(2)
    if c1.button("YES (It's a Business Service)"): navigate('res_bus_svc')
    if c2.button("NO"): navigate('check_tech_service')

# ---------------------------------------------------------
# STEP 6: TECHNICAL SERVICE CHECK (Q6 from Diagram)
# ---------------------------------------------------------
elif step == 'check_tech_service':
    st.subheader("Q6: Technical Service Check")
    st.markdown("### Is this a 'Utility' provided by IT to other IT teams?")
    st.info("e.g., Server Hosting, Storage, WiFi")
    st.markdown("**Example from Framework:** *'Tech Mgmt Service Client Hosting'*")

    c1, c2 = st.columns(2)
    if c1.button("YES (It's Technical)"): navigate('check_tech_offering')
    if c2.button("NO"): navigate('check_dynamic_ci')

# ---------------------------------------------------------
# STEP 6a: OFFERING CHECK (Q6a from Diagram)
# ---------------------------------------------------------
elif step == 'check_tech_offering':
    st.subheader("Q6a: Offering Check")
    st.markdown("### Is it a specific 'Plan Level' (Gold/Silver) of that utility?")
    st.markdown("**Example from Framework:** *'Tech Mgmt Service Offering Client Instance Backup'*")

    c1, c2 = st.columns(2)
    if c1.button("YES (It's an Offering)"): navigate('res_tech_off')
    if c2.button("NO (It's the Parent Service)"): navigate('res_tech_svc')

# ---------------------------------------------------------
# STEP 7: DYNAMIC CI GROUP CHECK (Q7 from Diagram)
# ---------------------------------------------------------
elif step == 'check_dynamic_ci':
    st.subheader("Q7: Dynamic CI Group Check")
    st.markdown("### Is this an automated 'Smart List' of servers/devices?")
    st.markdown("**Example from Framework:** *'Dynamic CI Group Client User Group - Win'*")

    c1, c2 = st.columns(2)
    if c1.button("YES (Dynamic Group)"): navigate('res_dyn_ci')
    if c2.button("NO (Unknown)"): navigate('res_unknown')


# --- RESULTS SCREEN (Strictly Mapped to Diagram Names) ---
def show_result(name, domain_class, explanation):
    st.markdown(f"""<div class="{domain_class}"><h2>✅ Result: {name}</h2><p>{explanation}</p></div>""", unsafe_allow_html=True)
    st.write("")
    if st.button("Start Over"): restart()

if step == 'res_bus_cap':
    show_result("Business Capability", "design", "Strategy/Design Domain. Defines WHAT we do.")
elif step == 'res_svc_port':
    show_result("Service Portfolio", "consume", "Consume Domain. A container/grouping for services.")
elif step == 'res_bus_app':
    show_result("Business Application", "design", "Design Domain. The Software Product (Brand).")
elif step == 'res_app_svc':
    show_result("Application Service", "manage", "Manage Tech Domain. The Running Instance (e.g. PROD).")
elif step == 'res_bus_svc':
    show_result("Business Service", "consume", "Consume Domain. An action for business users.")
elif step == 'res_tech_svc':
    show_result("Tech Mgmt Service", "manage", "Manage Tech Domain. IT-to-IT Utility Service.")
elif step == 'res_tech_off':
    show_result("Tech Mgmt Service Offering", "manage", "Manage Tech Domain. Specific SLA/Tier.")
elif step == 'res_dyn_ci':
    show_result("Dynamic CI Group", "manage", "Foundation/Manage Domain. Automated Group of CIs.")
elif step == 'res_unknown':
    st.error("Result: Unknown / Edge Case")
    st.write("Please check if this is a standard Infrastructure CI (Server, Switch, Printer).")
    if st.button("Start Over"): restart()
