import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="CSDM Classifier Pro", page_icon="🧊", layout="wide")

# --- STYLES ---
st.markdown("""
<style>
    .design { border-left: 6px solid #00B5AD; background-color: #F0FBFC; padding: 15px; }
    .manage { border-left: 6px solid #F2711C; background-color: #FEF6F1; padding: 15px; }
    .consume { border-left: 6px solid #21BA45; background-color: #F0FDF4; padding: 15px; }
    .explanation-box { background-color: #fff; border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    .example-list { background-color: #fafafa; padding: 10px; border-radius: 5px; border: 1px dashed #ccc; }
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
    st.title("CSDM Classifier Tool")
    st.caption("Standardized Classification & Naming Assistant")
st.divider()

step = st.session_state.step

# ---------------------------------------------------------
# STEP 1: BUSINESS CAPABILITY (Now with Layman Explanation)
# ---------------------------------------------------------
if step == 'start':
    st.subheader("Step 1: Business Capability Check")
    st.markdown("### Is this a high-level business 'Ability' or 'Function'?")
    
    st.markdown("""
    <div class="explanation-box">
        <h4>🛑 Layman's Terms: The "Resume Skill" Analogy</h4>
        <p>Think of a Business Capability as a <strong>Skill on a Resume</strong>.</p>
        <ul>
            <li><strong>The Skill:</strong> "Project Management" (This is the Capability).</li>
            <li><strong>The Tool:</strong> "Microsoft Excel" or "Jira" (This is the Application).</li>
        </ul>
        <hr>
        <h4>🧪 The "Stable Strategy" Test</h4>
        <p>If we fired the entire IT department and threw away all computers, would the business <em>still need to do this</em>?</p>
        <ul>
            <li><strong>YES:</strong> "We still need to do <em>Recruiting</em>." (This is a <strong>Business Capability</strong>).</li>
            <li><strong>NO:</strong> "We cannot do <em>Zoom</em> without computers." (Zoom is just a tool/Application).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    if c1.button("YES (It's a Strategic Ability)"): navigate('res_bus_cap')
    if c2.button("NO (It's something else)"): navigate('check_portfolio')

# ---------------------------------------------------------
# STEP 2: SERVICE PORTFOLIO
# ---------------------------------------------------------
elif step == 'check_portfolio':
    st.subheader("Step 2: Service Portfolio Check")
    st.markdown("### Is this the 'Menu' or the 'Food'?")
    
    st.markdown("""
    <div class="explanation-box">
        <h4>🛑 Layman's Terms: The Restaurant Analogy</h4>
        <p>A <strong>Service Portfolio</strong> is the <strong>Menu</strong> (e.g., "The Lunch Menu").</p>
        <ul>
            <li>You cannot "eat" the Menu. You cannot "fix" the Menu.</li>
            <li>It is just a container that lists the available services.</li>
        </ul>
        <p><em>If your item is just a grouping folder for reporting, say YES.</em></p>
    </div>
    """, unsafe_allow_html=True)
    
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


# --- UPDATED RESULT SCREEN (With 8-10 Examples) ---
def show_result(title, domain, style, definition, template, examples):
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
        st.subheader("📝 Naming Recommendation")
        st.success(f"**Template:** `{template}`")
        st.caption("Use this pattern to ensure consistency.")
        
    with c2:
        st.subheader("🏢 Industry Examples")
        # Creating a bulleted list from the array
        example_html = "".join([f"<li>{ex}</li>" for ex in examples])
        st.markdown(f"""
        <div class="example-list">
            <ul>{example_html}</ul>
        </div>
        """, unsafe_allow_html=True)

    # 3. Restart
    st.divider()
    if st.button("Start Over"): restart()

# --- RESULT DATA LOOKUP ---

if step == 'res_bus_cap':
    show_result(
        title="Business Capability", 
        domain="Design", 
        style="design", 
        definition="The 'What'. Strategy. Exists without IT.",
        template="[Region] - [Function] Management",
        examples=[
            "Global Recruiting Management",
            "Payment Processing",
            "Customer Relationship Management",
            "Supply Chain Logistics",
            "IT Asset Management",
            "Market Research",
            "Regulatory Compliance",
            "Disaster Recovery Planning"
        ]
    )

elif step == 'res_svc_port':
    show_result(
        title="Service Portfolio", 
        domain="Consume", 
        style="consume", 
        definition="The Menu. A container for services.",
        template="[Topic] Services Portfolio",
        examples=[
            "HR Services Portfolio",
            "IT Support Services",
            "Legal Services Portfolio",
            "Facility Management Services",
            "Digital Sales Enablement",
            "Employee Wellness Portfolio",
            "Financial Advisory Services",
            "Security & Access Services"
        ]
    )

elif step == 'res_bus_app':
    show_result(
        title="Business Application", 
        domain="Design", 
        style="design", 
        definition="The Product/Brand. Used for Budgeting.",
        template="[Vendor] [Product Name]",
        examples=[
            "Microsoft Teams",
            "Salesforce Sales Cloud",
            "Workday HCM",
            "SAP S/4HANA",
            "ServiceNow ITSM",
            "Adobe Creative Cloud",
            "Atlassian Jira",
            "Zoom Meeting",
            "Oracle NetSuite"
        ]
    )

elif step == 'res_app_svc':
    show_result(
        title="Application Service", 
        domain="Manage Tech", 
        style="manage", 
        definition="The Running Instance. Used for Incidents.",
        template="[App Name] - [Environment] - [Region]",
        examples=[
            "Zoom - Production - NA",
            "Workday - Test - Global",
            "SAP ERP - Dev - Europe",
            "ServiceNow - Sandbox",
            "Salesforce - UAT - Asia",
            "Jira - Disaster Recovery",
            "Exchange - Cluster A",
            "SharePoint - Corp Intranet - Prod"
        ]
    )

elif step == 'res_bus_svc':
    show_result(
        title="Business Service", 
        domain="Consume", 
        style="consume", 
        definition="User Action / Request.",
        template="[Verb] [Noun]",
        examples=[
            "Onboard New Employee",
            "Reset Password",
            "Request New Laptop",
            "Report WiFi Issue",
            "Grant VPN Access",
            "Book Conference Room",
            "Request Leave of Absence",
            "Update Emergency Contact",
            "Download Payslip"
        ]
    )

elif step == 'res_tech_svc':
    show_result(
        title="Technical Service", 
        domain="Manage Tech", 
        style="manage", 
        definition="IT Utility Service.",
        template="[Technology] [Service Type]",
        examples=[
            "Windows Server Hosting",
            "Oracle Database Management",
            "Network Connectivity",
            "Storage Area Network (SAN)",
            "Active Directory Management",
            "Data Center Cooling",
            "Firewall Administration",
            "Load Balancing Services"
        ]
    )

elif step == 'res_tech_off':
    show_result(
        title="Technical Service Offering", 
        domain="Manage Tech", 
        style="manage", 
        definition="Specific SLA Tier.",
        template="[Service] - [Tier]",
        examples=[
            "Windows Hosting - Gold",
            "Windows Hosting - Silver",
            "Storage - High Performance (SSD)",
            "Storage - Archive (Tape)",
            "Network - Dedicated Fiber",
            "Database - 24/7 Critical Support",
            "Laptop Support - Standard",
            "Laptop Support - VIP/Executive"
        ]
    )

elif step == 'res_dyn_ci':
    show_result(
        title="Dynamic CI Group", 
        domain="Foundation", 
        style="manage", 
        definition="Automated Group of CIs.",
        template="Grp - [Resource Type] - [Criteria]",
        examples=[
            "All Windows Servers - NY",
            "All Oracle Databases - Prod",
            "Linux Servers - AWS East",
            "Cisco Switches - Building A",
            "Workstations - Finance Dept",
            "VDI Instances - Tokyo",
            "Meraki Access Points - Floor 2"
        ]
    )

elif step == 'res_unknown':
    st.error("Unknown / Infrastructure CI")
    st.write("This is likely a Server, Switch, or Printer.")
    if st.button("Start Over"): restart()
