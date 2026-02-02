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
    .naming-box { border: 1px dashed #444; padding: 15px; border-radius: 5px; background-color: #fafafa; }
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
    st.caption("Standardized Naming & Classification Tool")
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
# STEP 2: SERVICE PORTFOLIO
# ---------------------------------------------------------
elif step == 'check_portfolio':
    st.subheader("Step 2: Service Portfolio Check")
    st.markdown("### Is this the 'Menu' or the 'Food'?")
    
    st.markdown("""
    <div class="explanation-box">
        <h4>🛑 The Restaurant Analogy</h4>
        <p>A <strong>Service Portfolio</strong> is the <strong>Menu</strong> (e.g., "Lunch Menu"). You cannot "order" the menu itself.</p>
        <p>A <strong>Service</strong> is the <strong>Food</strong> (e.g., "Burger"). You order the food.</p>
    </div>
    """, unsafe_allow_html=True)
    st.warning("Is this item just a grouping (The Menu)?")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (It is the Menu/Portfolio)"): navigate('res_svc_port')
    if c2.button("NO (It is the Food/Service)"): navigate('check_software')

# ---------------------------------------------------------
# STEP 3: BUSINESS APPLICATION
# ---------------------------------------------------------
elif step == 'check_software':
    st.subheader("Step 3: Business Application Check")
    st.markdown("### Is this a named Software Product we buy and track?")
    st.info("The 'Brand Name' in our inventory.")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Business App)"): navigate('res_bus_app')
    if c2.button("NO"): navigate('check_app_svc')

# ---------------------------------------------------------
# STEP 4: APPLICATION SERVICE
# ---------------------------------------------------------
elif step == 'check_app_svc':
    st.subheader("Step 4: Application Service Check")
    st.markdown("### Is this a specific RUNNING login page or environment?")
    st.warning("The thing that actually breaks.")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (App Service)"): navigate('res_app_svc')
    if c2.button("NO"): navigate('check_bus_svc')

# ---------------------------------------------------------
# STEP 5: BUSINESS SERVICE
# ---------------------------------------------------------
elif step == 'check_bus_svc':
    st.subheader("Step 5: Business Service Check")
    st.markdown("### Is this 'Help' or an 'Action' a user requests?")
    st.info("Something found in the Service Catalog.")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Business Service)"): navigate('res_bus_svc')
    if c2.button("NO"): navigate('check_tech_svc')

# ---------------------------------------------------------
# STEP 6: TECHNICAL SERVICE
# ---------------------------------------------------------
elif step == 'check_tech_svc':
    st.subheader("Step 6: Technical Service Check")
    st.markdown("### Is this a 'Utility' provided by IT to other IT teams?")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Technical Service)"): navigate('check_offering')
    if c2.button("NO"): navigate('check_dynamic')

# ---------------------------------------------------------
# STEP 6a: SERVICE OFFERING
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


# --- UPDATED RESULT SCREEN (With Naming Standards) ---
def show_result(title, domain, style, definition, std_fmt, std_ex, org_fmt):
    # 1. Classification Result
    st.markdown(f"""
    <div class="{style}">
        <h2>✅ Classification: {title}</h2>
        <p><strong>Domain:</strong> {domain}</p>
        <p><em>{definition}</em></p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    
    # 2. Naming Standards Columns
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("🌍 Industry Standard")
        st.info(f"**Format:** `{std_fmt}`")
        st.caption(f"Example: {std_ex}")
        
    with c2:
        st.subheader("🏢 CubeSimple Format")
        st.success(f"**Template:** `{org_fmt}`")
        st.caption("Copy this format for your CMDB request.")

    # 3. Copy Button (Simulation)
    st.divider()
    if st.button("Start Over"): restart()

# --- RESULT DATA LOOKUP ---

if step == 'res_bus_cap':
    show_result(
        title="Business Capability", 
        domain="Design", 
        style="design", 
        definition="The 'What'. Strategy. Exists without IT.",
        std_fmt="[Noun] Management",
        std_ex="Recruiting Management",
        org_fmt="[Region] - [Function] Management"
    )

elif step == 'res_svc_port':
    show_result(
        title="Service Portfolio", 
        domain="Consume", 
        style="consume", 
        definition="The Menu. A container for services.",
        std_fmt="[Topic] Services",
        std_ex="HR Services",
        org_fmt="Portfolio: [Department] Services"
    )

elif step == 'res_bus_app':
    show_result(
        title="Business Application", 
        domain="Design", 
        style="design", 
        definition="The Product/Brand. Used for Budgeting.",
        std_fmt="[Vendor] [Product]",
        std_ex="Microsoft Excel",
        org_fmt="[Vendor] [Product] (Global)"
    )

elif step == 'res_app_svc':
    show_result(
        title="Application Service", 
        domain="Manage Tech", 
        style="manage", 
        definition="The Running Instance. Used for Incidents.",
        std_fmt="[App] - [Environment]",
        std_ex="Zoom - Production",
        org_fmt="[App Name] - [Prod/Dev/Test] - [Region]"
    )

elif step == 'res_bus_svc':
    show_result(
        title="Business Service", 
        domain="Consume", 
        style="consume", 
        definition="User Action / Request.",
        std_fmt="[Verb] [Noun]",
        std_ex="Onboard New Employee",
        org_fmt="[Verb] [Noun] (Service)"
    )

elif step == 'res_tech_svc':
    show_result(
        title="Technical Service", 
        domain="Manage Tech", 
        style="manage", 
        definition="IT Utility Service.",
        std_fmt="[Tech] [Service Type]",
        std_ex="Windows Hosting",
        org_fmt="[Technology] [Hosting/Support]"
    )

elif step == 'res_tech_off':
    show_result(
        title="Technical Service Offering", 
        domain="Manage Tech", 
        style="manage", 
        definition="Specific SLA Tier.",
        std_fmt="[Service] - [Tier]",
        std_ex="Windows Hosting - Gold",
        org_fmt="[Service] - [Tier] ([SLA %])"
    )

elif step == 'res_dyn_ci':
    show_result(
        title="Dynamic CI Group", 
        domain="Foundation", 
        style="manage", 
        definition="Automated Group of CIs.",
        std_fmt="[Resource] - [Group Type]",
        std_ex="All Windows Servers - NY",
        org_fmt="Grp - [Resource Type] - [Location]"
    )

elif step == 'res_unknown':
    st.error("Unknown / Infrastructure CI")
    st.write("This is likely a Server, Switch, or Printer.")
    if st.button("Start Over"): restart()
