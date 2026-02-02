import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="CubeSimple CSDM Framework", page_icon="🧊", layout="wide")

# --- STYLES ---
st.markdown("""
<style>
    .design { border-left: 5px solid #00B5AD; background-color: #F0FBFC; padding: 15px; border-radius: 5px; }
    .manage { border-left: 5px solid #F2711C; background-color: #FEF6F1; padding: 15px; border-radius: 5px; }
    .consume { border-left: 5px solid #21BA45; background-color: #F0FDF4; padding: 15px; border-radius: 5px; }
    .foundation { border-left: 5px solid #767676; background-color: #F9F9F9; padding: 15px; border-radius: 5px; }
    .example-box { border: 1px solid #ddd; padding: 10px; border-radius: 5px; margin-top: 10px; background-color: #fff; }
</style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'step' not in st.session_state: st.session_state.step = 'start'
if 'show_example' not in st.session_state: st.session_state.show_example = False

def navigate(next_step):
    st.session_state.step = next_step
    st.rerun()

def restart():
    st.session_state.step = 'start'
    st.rerun()

def toggle_example():
    st.session_state.show_example = not st.session_state.show_example

# --- HELPER: ACME CORP EXAMPLE ---
def show_acme_example():
    with st.expander("📚 Read the 'ACME Corp' Example Story", expanded=True):
        st.markdown("""
        **Scenario:** ACME Corp needs to pay its employees. Here is how CSDM maps it:
        
        1. **Business Capability (Strategy):**
           * *Name:* "Payroll Management"
           * *Why:* This is **WHAT** we do. Even without computers, we must do this.
           
        2. **Business Application (Design):**
           * *Name:* "Workday"
           * *Why:* This is the software **Product** we bought. We pay a license for "Workday".
           * *Mapping:* One Capability (Payroll) can use many Apps (Workday, ADP, Excel).
           
        3. **Application Service (Manage Tech):**
           * *Name:* "Workday - Production"
           * *Why:* This is the **Live Instance** people log into. If this breaks, it's an Incident.
           * *Note:* We also have "Workday - Test", which is a *different* Application Service.
           
        4. **Business Service (Consume):**
           * *Name:* "Onboard New Employee"
           * *Why:* This is the **Action** an HR manager requests from the Service Portal.
           
        5. **Technical Service (Manage Tech):**
           * *Name:* "Database Hosting"
           * *Why:* The IT team manages this to keep Workday running. HR doesn't care about it.
        """)

# --- MAIN HEADER ---
col1, col2 = st.columns([1, 6])
with col1: st.write("# 🧊")
with col2: 
    st.title("CubeSimple CSDM Framework")
    st.caption("Aligned to CSDM v4.0 & Your Decision Tree")

if st.button("📖 Don't understand the terms? Click here for an Example"):
    toggle_example()

if st.session_state.show_example:
    show_acme_example()

st.divider()

# --- WIZARD LOGIC ---
step = st.session_state.step

# STEP 1
if step == 'start':
    st.subheader("Step 1: Strategic Strategy")
    st.markdown("### Is this a high-level Business Ability?")
    st.info("Does this ability exist even if we have NO computers? (e.g. 'Recruiting')")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Capability)"): navigate('res_bus_cap')
    if c2.button("NO (Check Next)"): navigate('q_portfolio')

# STEP 2
elif step == 'q_portfolio':
    st.subheader("Step 2: Container Check")
    st.markdown("### Is this just a 'Folder' or 'Category'?")
    st.warning("You cannot 'order' this or 'fix' this. It just holds other services.")
    
    c1, c2 = st.columns(2)
    if c1.button("YES (Portfolio)"): navigate('res_svc_port')
    if c2.button("NO (Check Next)"): navigate('q_software')

# STEP 3
elif step == 'q_software':
    st.subheader("Step 3: Software Check")
    st.markdown("### Does this represent a Software Product?")
    
    c1, c2 = st.columns(2)
    if c1.button("YES"): navigate('split_software')
    if c2.button("NO"): navigate('q_service')

# STEP 3a (SPLIT)
elif step == 'split_software':
    st.error("⚠️ CRITICAL DECISION")
    st.write("You selected Software. Now, are you talking about the **BRAND** or the **INSTANCE**?")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Option A: The Brand**")
        st.write("*Example:* 'Workday' (The concept)")
        st.write("*Use:* Budgeting, Licensing, Architecture.")
        if st.button("It's the Brand (Business App)"): navigate('res_bus_app')
    with c2:
        st.warning("**Option B: The Instance**")
        st.write("*Example:* 'Workday - PROD' (The login site)")
        st.write("*Use:* Incidents, Change Mgmt, Monitoring.")
        if st.button("It's the Instance (App Service)"): navigate('res_app_svc')

# STEP 4
elif step == 'q_service':
    st.subheader("Step 4: Service Check")
    st.markdown("### Is this an Action/Help request?")
    st.write("Who is the customer asking for this?")
    
    c1, c2 = st.columns(2)
    if c1.button("Business User (HR, Finance)"): navigate('res_bus_svc')
    if c2.button("IT Team (Admins, Devs)"): navigate('q_tech_offering')

# STEP 5
elif step == 'q_tech_offering':
    st.subheader("Step 5: Technical Detail")
    st.markdown("### Is it a specific Tier/SLA?")
    st.write("Example: 'Gold Hosting' vs just 'Hosting'")
    
    c1, c2 = st.columns(2)
    if c1.button("Specific Tier (Offering)"): navigate('res_tech_off')
    if c2.button("General Service"): navigate('res_tech_svc')

# --- RESULTS ---
def show_result(title, domain, style, definition, example):
    st.markdown(f"""
    <div class="{style}">
        <h2>🎯 {title}</h2>
        <h4>Domain: {domain}</h4>
        <hr>
        <p><strong>Definition:</strong> {definition}</p>
        <p><strong>Example:</strong> {example}</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    if st.button("Start Over"): restart()

if step == 'res_bus_cap':
    show_result("Business Capability", "Design", "design", "Strategy/What we do.", "Payroll Management")
elif step == 'res_svc_port':
    show_result("Service Portfolio", "Consume", "consume", "A container/grouping.", "HR Services")
elif step == 'res_bus_app':
    show_result("Business Application", "Design", "design", "The Product/Brand. Maps 1-to-Many to Capabilities.", "Workday")
elif step == 'res_app_svc':
    show_result("Application Service", "Manage Tech", "manage", "The Running Instance/Stack.", "Workday - PROD")
elif step == 'res_bus_svc':
    show_result("Business Service", "Consume", "consume", "User Action.", "Onboard Employee")
elif step == 'res_tech_svc':
    show_result("Technical Service", "Manage Tech", "manage", "IT Utility.", "Server Hosting")
elif step == 'res_tech_off':
    show_result("Tech Service Offering", "Manage Tech", "manage", "Service + SLA.", "Gold Hosting")
