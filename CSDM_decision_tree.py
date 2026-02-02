import streamlit as st

# --- CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="CubeSimple CSDM v4 Framework", 
    page_icon="🧊",
    layout="wide"
)

# Custom CSS to match CSDM Domain Colors
st.markdown("""
<style>
    .design-domain { border-left: 5px solid #00B5AD; padding: 10px; background-color: #f0fbfc; }
    .manage-domain { border-left: 5px solid #F2711C; padding: 10px; background-color: #fef6f1; }
    .consume-domain { border-left: 5px solid #21BA45; padding: 10px; background-color: #f0fdf4; }
    .foundation-domain { border-left: 5px solid #767676; padding: 10px; background-color: #f9f9f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
def init_state():
    if 'step' not in st.session_state:
        st.session_state.step = 'start'
    if 'history' not in st.session_state:
        st.session_state.history = []

def navigate(next_step):
    """Moves to the next step and IMMEDIATELY reruns the app."""
    st.session_state.history.append(st.session_state.step)
    st.session_state.step = next_step
    st.rerun()  # <--- THIS FIXES THE DOUBLE CLICK ISSUE

def go_back():
    """Moves back one step and IMMEDIATELY reruns the app."""
    if st.session_state.history:
        st.session_state.step = st.session_state.history.pop()
        st.rerun() # <--- THIS FIXES THE DOUBLE CLICK ISSUE

def restart():
    """Resets the app and IMMEDIATELY reruns."""
    st.session_state.step = 'start'
    st.session_state.history = []
    st.rerun() # <--- THIS FIXES THE DOUBLE CLICK ISSUE

# --- UI COMPONENTS ---
def show_header():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown("# 🧊")
    with col2:
        st.title("CubeSimple CSDM v4 Framework")
        st.caption("ServiceNow Common Service Data Model Decision Wizard")
    st.divider()

def show_card(title, definition, litmus_test, examples, context_color="gray"):
    """Displays a definition card with a specific domain color."""
    colors = {
        "design": "#00B5AD", # Teal
        "manage": "#F2711C", # Orange
        "consume": "#21BA45", # Green
        "foundation": "#767676" # Grey
    }
    color = colors.get(context_color, "#767676")
    
    st.markdown(f"""
    <div style="border: 1px solid #ddd; border-top: 5px solid {color}; border-radius: 5px; padding: 15px; margin-bottom: 20px;">
        <h3>{title}</h3>
        <p><strong>📖 Definition:</strong> {definition}</p>
        <p><strong>🧪 Litmus Test:</strong> <em>{litmus_test}</em></p>
        <p><strong>✅ Examples:</strong> {examples}</p>
    </div>
    """, unsafe_allow_html=True)

def show_result(title, domain, domain_class, definition, example, naming_std):
    """Displays the final result."""
    
    # Domain badges
    domain_map = {
        "Design": "design-domain",
        "Manage Technical": "manage-domain",
        "Sell/Consume": "consume-domain",
        "Foundation": "foundation-domain"
    }
    css_class = domain_map.get(domain, "foundation-domain")
    
    st.balloons()
    
    st.markdown(f"""
    <div class="{css_class}">
        <h2>🎯 Classification: {title}</h2>
        <h4>Domain: {domain}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📝 Definition")
        st.write(definition)
        st.info(f"**Example:** {example}")
        
    with col2:
        st.subheader("🏷️ Naming Standard")
        st.code(naming_std, language="text")
        st.caption("Copy this format for your request.")

    st.divider()
    if st.button("🔄 Classify Another Item"):
        restart()

# --- MAIN LOGIC FLOW ---
def main():
    init_state()
    show_header()
    
    step = st.session_state.step

    # ---------------- START ----------------
    if step == 'start':
        st.subheader("Step 1: The Strategy Check")
        show_card(
            title="Is this a High-Level Business Ability?",
            definition="An abstract ability of the organization (Strategy). It defines WHAT we do, not HOW.",
            litmus_test="Does this exist even without any computers? (e.g., We would still do 'Recruiting' with pen and paper).",
            examples="Recruiting, Payroll Processing, Logistics, Market Research",
            context_color="design"
        )
        c1, c2 = st.columns(2)
        if c1.button("Yes, it's a Business Ability"): navigate('res_bus_cap')
        if c2.button("No, it's something else"): navigate('check_container')

    # ---------------- CONTAINER CHECK ----------------
    elif step == 'check_container':
        st.subheader("Step 2: The Container Check")
        show_card(
            title="Is this just a Folder or Container?",
            definition="A logical grouping used for reporting. You cannot 'order' this directly.",
            litmus_test="Is this just a bucket to hold other services?",
            examples="HR Services, Communication Tools, IT Support Services",
            context_color="consume"
        )
        c1, c2 = st.columns(2)
        if c1.button("Yes, it's a Portfolio/Container"): navigate('res_svc_port')
        if c2.button("No, continue"): navigate('check_software')

    # ---------------- SOFTWARE BRANCH (CRITICAL SPLIT) ----------------
    elif step == 'check_software':
        st.subheader("Step 3: The Software Check")
        st.write("Does this represent a Software Product?")
        
        c1, c2 = st.columns(2)
        if c1.button("Yes, it involves Software"): navigate('software_split')
        if c2.button("No, it's a Service/Action"): navigate('check_service')

    elif step == 'software_split':
        st.warning("⚠️ Critical CSDM Decision Point")
        st.write("You selected Software. We must distinguish between the **Brand/Product** and the **Running Instance**.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("Option A: The Product Concept")
            st.markdown("""
            * Used for Planning, Costing, & Licensing.
            * Represents *all* instances (Dev/Test/Prod).
            * **Litmus Test:** Is this the name on the invoice from the vendor?
            """)
            if st.button("It's the Product (Concept)"): navigate('res_bus_app')
            
        with col2:
            st.warning("Option B: The Running Instance")
            st.markdown("""
            * Used for Operations, Incidents, & Changes.
            * It has a specific Environment (Prod/Dev).
            * **Litmus Test:** Can I log into this specific one right now?
            """)
            if st.button("It's the Running Instance"): navigate('res_app_svc')

    # ---------------- SERVICE BRANCH ----------------
    elif step == 'check_service':
        st.subheader("Step 4: The Service Type")
        show_card(
            title="Is this an Action or Help Request?",
            definition="Something a user interacts with to get value.",
            litmus_test="Who is the customer requesting this?",
            examples="Onboard Employee (User), Server Hosting (IT Admin)",
            context_color="consume"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("### The customer is a **Business User**")
            st.caption("(HR, Finance, Sales, Employee)")
            if st.button("Business User"): navigate('res_bus_svc')
            
        with col2:
            st.write("### The customer is an **IT Team**")
            st.caption("(Server Admins, Developers, Network Team)")
            if st.button("IT / Technical Team"): navigate('check_tech_svc_type')

    # ---------------- TECHNICAL SERVICE BRANCH ----------------
    elif step == 'check_tech_svc_type':
        st.subheader("Step 5: Technical Service Detail")
        st.write("We know it's for IT. Is this the **Service Itself** or a specific **Tier/Offering**?")
        
        show_card(
            title="Service vs. Offering",
            definition="An Offering is a specific flavor of the service with defined commitments (SLA/Price).",
            litmus_test="Does this have a tier (Gold/Silver) or specific SLA attached?",
            examples="Windows Hosting (Service) vs. Gold Windows Hosting (Offering)",
            context_color="manage"
        )
        
        c1, c2 = st.columns(2)
        if c1.button("It's a Specific Tier (Offering)"): navigate('res_tech_svc_off')
        if c2.button("It's the General Service"): navigate('res_tech_svc')

    # ---------------- RESULTS: DESIGN DOMAIN ----------------
    elif step == 'res_bus_cap':
        show_result(
            title="Business Capability",
            domain="Design",
            domain_class="design",
            definition="The highest level of abstraction. Represents WHAT the business does.",
            example="Global Recruiting, Logistics Management",
            naming_std="[Noun] [Management/Processing]"
        )

    elif step == 'res_bus_app':
        show_result(
            title="Business Application",
            domain="Design",
            domain_class="design",
            definition="The logical software product. Used for Portfolio Management. NOT for Incidents.",
            example="Zoom, Salesforce, SAP S/4HANA",
            naming_std="[Vendor] [Product Name]"
        )

    # ---------------- RESULTS: MANAGE TECHNICAL DOMAIN ----------------
    elif step == 'res_app_svc':
        show_result(
            title="Application Service",
            domain="Manage Technical",
            domain_class="manage",
            definition="The specific deployed stack. This is the Configuration Item (CI) for Incidents.",
            example="Zoom - Production, SAP - Dev, Workday - Test",
            naming_std="[App Name] - [Environment]"
        )

    elif step == 'res_tech_svc':
        show_result(
            title="Technical Service",
            domain="Manage Technical",
            domain_class="manage",
            definition="A service provided by IT to IT to support infrastructure.",
            example="Windows Server Hosting, Storage Management",
            naming_std="[Technology] [Hosting/Support]"
        )
        
    elif step == 'res_tech_svc_off':
        show_result(
            title="Technical Service Offering",
            domain="Manage Technical",
            domain_class="manage",
            definition="A specific option of a Technical Service with SLAs/Commitments.",
            example="Gold Windows Hosting (99.9%), Standard Storage",
            naming_std="[Service] - [Tier/SLA]"
        )

    # ---------------- RESULTS: CONSUME DOMAIN ----------------
    elif step == 'res_svc_port':
        show_result(
            title="Service Portfolio",
            domain="Sell/Consume",
            domain_class="consume",
            definition="A container used to group services for reporting.",
            example="HR Services, IT Support Services",
            naming_std="[Department/Topic] Services"
        )

    elif step == 'res_bus_svc':
        show_result(
            title="Business Service",
            domain="Sell/Consume",
            domain_class="consume",
            definition="A service consumed by business users to complete a task.",
            example="Onboard New Hire, Reset Password",
            naming_std="[Verb] [Noun]"
        )

    # ---------------- FOOTER ----------------
    if st.session_state.history:
        st.divider()
        if st.button("⬅️ Back"):
            go_back()

if __name__ == "__main__":
    main()
