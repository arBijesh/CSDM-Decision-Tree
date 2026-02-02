import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="CubeSimple CSDM Classifier", page_icon="🧊", layout="wide")

# --- STYLES (Aligned to your Framework Colors) ---
st.markdown("""
<style>
    .design { border-left: 6px solid #00B5AD; background-color: #F0FBFC; padding: 15px; }
    .manage { border-left: 6px solid #F2711C; background-color: #FEF6F1; padding: 15px; }
    .consume { border-left: 6px solid #21BA45; background-color: #F0FDF4; padding: 15px; }
    .example-box { border: 1px solid #ddd; background-color: #ffffff; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'step' not in st.session_state: st.session_state.step = 'start'
if 'show_acme' not in st.session_state: st.session_state.show_acme = False

def navigate(next_step):
    st.session_state.step = next_step
    st.rerun()

def restart():
    st.session_state.step = 'start'
    st.rerun()

def toggle_acme():
    st.session_state.show_acme = not st.session_state.show_acme

# --- ACME CORP EXAMPLE CONTENT ---
def show_acme_example():
    st.markdown("""
    <div class="example-box">
        <h3>🏢 Real-World Example: ACME Corp (HR Dept)</h3>
        <p><strong>Scenario:</strong> ACME Corp needs to pay its employees. Here is how we map it using strict CSDM terms:</p>
        <hr>
        
        <p><strong>1. Business Capability (Strategy)</strong><br>
        <em>Example:</em> "Payroll Management"<br>
        <em>Logic:</em> This is <strong>WHAT</strong> ACME does. It is a strategic ability. Even if all computers break, they still have the "Capability" to pay people (manual checks).</p>
        
        <p><strong>2. Service Portfolio (Consume)</strong><br>
        <em>Example:</em> "HR Services Portfolio"<br>
        <em>Logic:</em> This is just the <strong>Grouping</strong>. It holds all the specific HR services together for reporting. You can't "fix" a portfolio.</p>

        <p><strong>3. Business Application (Design)</strong><br>
        <em>Example:</em> "Workday"<br>
        <em>Logic:</em> This is the <strong>Software Product</strong> ACME bought. We pay a license fee for "Workday".<br>
        <em>Mapping Rule:</em> <strong>One</strong> Business Capability (Payroll) is supported by <strong>Many</strong> Business Applications (Workday, ADP, Excel).</p>

        <p><strong>4. Application Service (Manage Tech)</strong><br>
        <em>Example:</em> "Workday - Production"<br>
        <em>Logic:</em> This is the <strong>Running Instance</strong>. This is what you log into. If this goes down, it is an Incident.</p>

        <p><strong>5. Business Service (Consume)</strong><br>
        <em>Example:</em> "Onboard New Employee"<br>
        <em>Logic:</em> This is the <strong>Action</strong> an HR Manager requests from the Service Portal.</p>
        
        <p><strong>6. Technical Service (Manage Tech)</strong><br>
        <em>Example:</em> "Server Hosting"<br>
        <em>Logic:</em> The IT team provides this utility to keep the Application Service running.</p>
    </div>
    """, unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([1, 6])
with col1: st.title("🧊")
with col2: 
    st.title("CubeSimple CSDM Classifier")
    st.caption("Strict Alignment to CSDM Framework & Decision Tree")

if st.button("📖 Click here to see the ACME Corp Example"):
    toggle_acme()

if st.session_state.show_acme:
    show_acme_example()

st.divider()

# --- WIZARD LOGIC ---
step = st.session_state.step

# STEP 1
if step == 'start':
    st.subheader("Step 1: Business Capability Check")
    st.markdown("### Is this a high-level business 'Ability' or 'Function'?")
    st.info("Does it exist even without IT? (e.g., Recruiting, Payroll)")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Capability)"): navigate('res_bus_cap')
    if c2.button("NO"): navigate('check_portfolio')

# STEP 2 (STRICT NAME: SERVICE PORTFOLIO)
elif step == 'check_portfolio':
    st.subheader("Step 2: Service Portfolio Check")
    st.markdown("### Is this just a 'Category' or 'Folder' that holds other services?")
    st.warning("You cannot 'order' this directly. It is a grouping for reporting.")
    st.markdown("**Example:** *'Service Portfolio Digital Sales Enablement'*")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Portfolio)"): navigate('res_svc_port')
    if c2.button("NO"): navigate('check_software')

# STEP 3
elif step == 'check_software':
    st.subheader("Step 3: Business Application Check")
    st.markdown("### Is this a named Software Product we buy and track?")
    st.info("The 'Brand Name' in our inventory (for licensing/costs).")
    st.markdown("**Example:** *'Business Application Client CRM'*")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Business App)"): navigate('res_bus_app')
    if c2.button("NO"): navigate('check_app_svc')

# STEP 4
elif step == 'check_app_svc':
    st.subheader("Step 4: Application Service Check")
    st.markdown("### Is this a specific RUNNING login page or environment?")
    st.warning("The thing that actually breaks (Incidents/Change).")
    st.markdown("**Example:** *'Service Instance PROD - Client CRM'*")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (App Service)"): navigate('res_app_svc')
    if c2.button("NO"): navigate('check_bus_svc')

# STEP 5
elif step == 'check_bus_svc':
    st.subheader("Step 5: Business Service Check")
    st.markdown("### Is this 'Help' or an 'Action' a user requests?")
    st.info("Something found in the Service Catalog.")
    st.markdown("**Example:** *'Business Service Customer Lead Management'*")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Business Service)"): navigate('res_bus_svc')
    if c2.button("NO"): navigate('check_tech_svc')

# STEP 6
elif step == 'check_tech_svc':
    st.subheader("Step 6: Technical Service Check")
    st.markdown("### Is this a 'Utility' provided by IT to other IT teams?")
    st.info("e.g. Hosting, Storage, Network")
    st.markdown("**Example:** *'Tech Mgmt Service Client Hosting'*")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Technical Service)"): navigate('check_offering')
    if c2.button("NO"): navigate('check_dynamic')

# STEP 6a
elif step == 'check_offering':
    st.subheader("Step 6a: Service Offering Check")
    st.markdown("### Is it a specific 'Plan Level' (Gold/Silver) of that utility?")
    st.markdown("**Example:** *'Tech Mgmt Service Offering Client Instance Backup'*")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Offering)"): navigate('res_tech_off')
    if c2.button("NO (Parent Service)"): navigate('res_tech_svc')

# STEP 7
elif step == 'check_dynamic':
    st.subheader("Step 7: Dynamic CI Group Check")
    st.markdown("### Is this an automated 'Smart List' of devices?")
    st.markdown("**Example:** *'Dynamic CI Group Client User Group'*")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Dynamic Group)"): navigate('res_dyn_ci')
    if c2.button("NO (Unknown)"): navigate('res_unknown')

# --- RESULTS ---
def show_result(title, domain, style, definition):
    st.markdown(f"""
    <div class="{style}">
        <h2>✅ Result: {title}</h2>
        <p><strong>Domain:</strong> {domain}</p>
        <hr>
        <p>{definition}</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    if st.button("Start Over"): restart()

if step == 'res_bus_cap':
    show_result("Business Capability", "Design Domain", "design", "Strategy: What we do.")
elif step == 'res_svc_port':
    show_result("Service Portfolio", "Consume Domain", "consume", "A Grouping/Container for services.")
elif step == 'res_bus_app':
    show_result("Business Application", "Design Domain", "design", "The Software Product (Brand). Maps 1-to-Many to Capabilities.")
elif step == 'res_app_svc':
    show_result("Application Service", "Manage Tech Domain", "manage", "The Running Instance (Prod/Dev).")
elif step == 'res_bus_svc':
    show_result("Business Service", "Consume Domain", "consume", "User Action / Request.")
elif step == 'res_tech_svc':
    show_result("Technical Service", "Manage Tech Domain", "manage", "IT Utility Service.")
elif step == 'res_tech_off':
    show_result("Technical Service Offering", "Manage Tech Domain", "manage", "Specific SLA Tier (Gold/Silver).")
elif step == 'res_dyn_ci':
    show_result("Dynamic CI Group", "Foundation Domain", "manage", "Automated Group of CIs.")
elif step == 'res_unknown':
    st.error("Unknown / Infrastructure CI")
    st.write("This might be a Server, Switch, or Printer.")
    if st.button("Start Over"): restart()
