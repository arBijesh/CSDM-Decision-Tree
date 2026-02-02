import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="CubeSimple CSDM Classifier", page_icon="🧊", layout="wide")

# --- STYLES ---
st.markdown("""
<style>
    .design { border-left: 6px solid #00B5AD; background-color: #F0FBFC; padding: 15px; }
    .manage { border-left: 6px solid #F2711C; background-color: #FEF6F1; padding: 15px; }
    .consume { border-left: 6px solid #21BA45; background-color: #F0FDF4; padding: 15px; }
    .explanation-box { background-color: #fff; border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
if 'step' not in st.session_state: st.session_state.step = 'start'

def navigate(next_step):
    st.session_state.step = next_step
    st.rerun()

def restart():
    st.session_state.step = 'start'
    st.rerun()

# --- HEADER ---
col1, col2 = st.columns([1, 6])
with col1: st.title("🧊")
with col2: 
    st.title("CubeSimple CSDM Classifier")
    st.caption("Detailed Layman Explanations Enabled")
st.divider()

step = st.session_state.step

# ---------------------------------------------------------
# STEP 1: BUSINESS CAPABILITY
# ---------------------------------------------------------
if step == 'start':
    st.subheader("Step 1: Business Capability Check")
    st.markdown("### Is this a high-level business 'Ability' or 'Function'?")
    st.info("Does it exist even without IT? (e.g., Recruiting, Payroll)")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Capability)"): navigate('res_bus_cap')
    if c2.button("NO"): navigate('check_portfolio')

# ---------------------------------------------------------
# STEP 2: SERVICE PORTFOLIO CHECK (UPDATED DETAIL)
# ---------------------------------------------------------
elif step == 'check_portfolio':
    st.subheader("Step 2: Service Portfolio Check")
    st.markdown("### Is this the 'Menu' or the 'Food'?")
    
    st.markdown("""
    <div class="explanation-box">
        <h4>🛑 Stop and Think: The Restaurant Analogy</h4>
        <p>In CSDM, a <strong>Service Portfolio</strong> is like a <strong>Restaurant Menu</strong> (e.g., "The Lunch Menu").</p>
        <ul>
            <li>You cannot "eat" the Menu. (You cannot consume a Portfolio).</li>
            <li>You cannot "order" the Menu itself. (You can't submit a ticket for a Portfolio).</li>
            <li>It just <strong>lists</strong> the options available to customers.</li>
        </ul>
        <hr>
        <h4>🧪 The "Broken" Test</h4>
        <p>If a user says <em>"My [Item Name] is broken,"</em> does that make sense?</p>
        <ul>
            <li><strong>NO:</strong> "My <em>Digital Sales Enablement</em> is broken." (This sounds wrong. It's too broad. This is a <strong>Portfolio</strong>).</li>
            <li><strong>YES:</strong> "My <em>Customer Lead Management</em> is broken." (This makes sense. This is a <strong>Service</strong>).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.warning("Decision: Is this item just the 'Menu' (a grouping) that users look at to find other things?")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (It is the Menu/Portfolio)"): navigate('res_svc_port')
    if c2.button("NO (It is an actual Service/App)"): navigate('check_software')

# ---------------------------------------------------------
# STEP 3: BUSINESS APPLICATION CHECK
# ---------------------------------------------------------
elif step == 'check_software':
    st.subheader("Step 3: Business Application Check")
    st.markdown("### Is this a named Software Product we buy and track?")
    st.info("The 'Brand Name' in our inventory.")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Business App)"): navigate('res_bus_app')
    if c2.button("NO"): navigate('check_app_svc')

# ---------------------------------------------------------
# STEP 4: APPLICATION SERVICE CHECK
# ---------------------------------------------------------
elif step == 'check_app_svc':
    st.subheader("Step 4: Application Service Check")
    st.markdown("### Is this a specific RUNNING login page or environment?")
    st.warning("The thing that actually breaks.")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (App Service)"): navigate('res_app_svc')
    if c2.button("NO"): navigate('check_bus_svc')

# ---------------------------------------------------------
# STEP 5: BUSINESS SERVICE CHECK
# ---------------------------------------------------------
elif step == 'check_bus_svc':
    st.subheader("Step 5: Business Service Check")
    st.markdown("### Is this 'Help' or an 'Action' a user requests?")
    st.info("Something found in the Service Catalog.")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Business Service)"): navigate('res_bus_svc')
    if c2.button("NO"): navigate('check_tech_svc')

# ---------------------------------------------------------
# STEP 6: TECHNICAL SERVICE CHECK
# ---------------------------------------------------------
elif step == 'check_tech_svc':
    st.subheader("Step 6: Technical Service Check")
    st.markdown("### Is this a 'Utility' provided by IT to other IT teams?")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Technical Service)"): navigate('check_offering')
    if c2.button("NO"): navigate('check_dynamic')

# ---------------------------------------------------------
# STEP 6a: OFFERING CHECK
# ---------------------------------------------------------
elif step == 'check_offering':
    st.subheader("Step 6a: Service Offering Check")
    st.markdown("### Is it a specific 'Plan Level' (Gold/Silver) of that utility?")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Offering)"): navigate('res_tech_off')
    if c2.button("NO (Parent Service)"): navigate('res_tech_svc')

# ---------------------------------------------------------
# STEP 7: DYNAMIC CI GROUP
# ---------------------------------------------------------
elif step == 'check_dynamic':
    st.subheader("Step 7: Dynamic CI Group Check")
    st.markdown("### Is this an automated 'Smart List' of devices?")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Dynamic Group)"): navigate('res_dyn_ci')
    if c2.button("NO (Unknown)"): navigate('res_unknown')


# --- RESULTS SCREEN ---
def show_result(name, domain_class, explanation):
    st.markdown(f"""<div class="{domain_class}"><h2>✅ Result: {name}</h2><p>{explanation}</p></div>""", unsafe_allow_html=True)
    st.write("")
    if st.button("Start Over"): restart()

if step == 'res_bus_cap': show_result("Business Capability", "design", "Strategy/Design Domain. Defines WHAT we do.")
elif step == 'res_svc_port': show_result("Service Portfolio", "consume", "Consume Domain. A container/grouping for services.")
elif step == 'res_bus_app': show_result("Business Application", "design", "Design Domain. The Software Product (Brand).")
elif step == 'res_app_svc': show_result("Application Service", "manage", "Manage Tech Domain. The Running Instance.")
elif step == 'res_bus_svc': show_result("Business Service", "consume", "Consume Domain. An action for business users.")
elif step == 'res_tech_svc': show_result("Tech Mgmt Service", "manage", "Manage Tech Domain. IT-to-IT Utility Service.")
elif step == 'res_tech_off': show_result("Tech Mgmt Service Offering", "manage", "Manage Tech Domain. Specific SLA/Tier.")
elif step == 'res_dyn_ci': show_result("Dynamic CI Group", "manage", "Foundation/Manage Domain. Automated Group of CIs.")
elif step == 'res_unknown': 
    st.error("Unknown / Infrastructure CI")
    if st.button("Start Over"): restart()
