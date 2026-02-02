import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="CubeSimple CSDM Wizard", 
    page_icon="🧊",
    layout="centered"
)

# --- SESSION STATE MANAGEMENT ---
def init_state():
    """Initialize the session state variables to track progress."""
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 'q1'
    if 'history' not in st.session_state:
        st.session_state.history = []

def navigate_to(step):
    """Move to the next step and save history for the back button."""
    st.session_state.history.append(st.session_state.current_step)
    st.session_state.current_step = step

def go_back():
    """Go back to the previous step."""
    if st.session_state.history:
        st.session_state.current_step = st.session_state.history.pop()

def restart():
    """Reset the application to the start."""
    st.session_state.current_step = 'q1'
    st.session_state.history = []

# --- UI COMPONENTS ---
def show_header():
    """Displays the branded header."""
    st.title("🧊 CubeSimple CSDM Assistant")
    st.markdown("""
    **ServiceNow Common Service Data Model (CSDM) Classifier**
    
    Use this tool to determine the correct CSDM table and naming convention for your item.
    """)
    st.markdown("---")

def show_question(title, question, examples, yes_target, no_target, tip=None):
    """Reusable function to display a question step."""
    st.subheader(title)
    st.markdown(f"### {question}")
    
    if examples:
        st.info(f"**Examples:** {examples}")
    
    if tip:
        st.caption(f"💡 {tip}")
    
    st.write("") # Spacer
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes ✅", use_container_width=True):
            navigate_to(yes_target)
    with col2:
        if st.button("No ❌", use_container_width=True):
            navigate_to(no_target)

def show_result(table_name, domain, definition, naming_convention):
    """Reusable function to display the final result."""
    st.balloons()
    st.success(f"### Result: {table_name}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("CSDM Domain", domain)
    with col2:
        st.metric("ServiceNow Table", table_name.replace(" ", "_").lower())
    
    st.markdown("### 📖 Definition")
    st.write(definition)
    
    st.markdown("---")
    st.subheader("📝 Naming Standard")
    st.code(naming_convention, language="text")
    st.caption("Please use the format above when creating this item in ServiceNow.")
    
    st.markdown("---")
    if st.button("🔄 Classify Another Item", use_container_width=True):
        restart()

# --- MAIN APP LOGIC ---
def main():
    init_state()
    show_header()
    
    step = st.session_state.current_step

    # ---------------- QUESTIONS ----------------
    
    if step == 'q1':
        show_question(
            title="Step 1: Business Capability",
            question="Is this a high-level business 'Ability' or 'Function'?",
            examples="Recruiting, Payroll, Logistics",
            tip="Does this ability exist even without IT? (e.g. We would still do 'Recruiting' even with pen and paper)",
            yes_target='res_bus_cap',
            no_target='q2'
        )

    elif step == 'q2':
        show_question(
            title="Step 2: Service Portfolio",
            question="Is this just a 'Category' or 'Folder' that holds other services?",
            examples="HR Services, Communication Tools, IT Support",
            tip="You cannot 'order' this directly; it is just a container to group things.",
            yes_target='res_svc_port',
            no_target='q3'
        )

    elif step == 'q3':
        show_question(
            title="Step 3: Business Application",
            question="Is this a named Software Product we buy and track?",
            examples="Workday, Salesforce, Zoom, Microsoft Excel",
            tip="This is the 'Brand Name' in our inventory used for planning and costs.",
            yes_target='res_bus_app',
            no_target='q4'
        )

    elif step == 'q4':
        show_question(
            title="Step 4: Application Service",
            question="Is this a specific RUNNING login page or environment?",
            examples="Zoom - Production, SAP - Dev, Workday - Test",
            tip="This is the thing that actually breaks. It has a URL or an infrastructure stack.",
            yes_target='res_app_svc',
            no_target='q5'
        )

    elif step == 'q5':
        show_question(
            title="Step 5: Business Service",
            question="Is this 'Help' or an 'Action' a user requests to do their job?",
            examples="Onboard Employee, Fix my Email, Request New Laptop",
            tip="Something found in the Service Catalog that a user clicks to get help.",
            yes_target='res_bus_svc',
            no_target='q6'
        )

    elif step == 'q6':
        show_question(
            title="Step 6: Technical Service",
            question="Is this a 'Utility' provided by IT to other IT teams?",
            examples="Server Hosting, Storage, Wi-Fi, Database Support",
            tip="Business users usually don't know about this; it supports other apps.",
            yes_target='q6a',
            no_target='q7'
        )

    elif step == 'q6a':
        show_question(
            title="Step 6a: Service Offering",
            question="Is it a specific 'Plan Level' (Gold/Silver) of that utility?",
            examples="Gold Hosting (99.9% Uptime), Standard Storage",
            tip="Does it have specific SLA commitments attached to it?",
            yes_target='res_tech_svc_off',
            no_target='res_tech_svc'
        )

    elif step == 'q7':
        show_question(
            title="Step 7: Dynamic CI Group",
            question="Is this an automated 'Smart List' of servers or devices?",
            examples="All Windows Servers in NY, All Oracle Databases",
            tip="It is not a single server, but a dynamic group based on a query.",
            yes_target='res_dyn_ci',
            no_target='res_unknown'
        )

    # ---------------- RESULTS ----------------

    elif step == 'res_bus_cap':
        show_result(
            table_name="Business Capability",
            domain="Design Domain",
            definition="The 'What' we do. A high-level abstract capability of the organization.",
            naming_convention="[Capability Name] (e.g., 'Recruiting')"
        )

    elif step == 'res_svc_port':
        show_result(
            table_name="Service Portfolio",
            domain="Consume Domain",
            definition="A logical container for services. Used to group services for reporting.",
            naming_convention="[Portfolio Name] (e.g., 'HR Services')"
        )

    elif step == 'res_bus_app':
        show_result(
            table_name="Business Application",
            domain="Design Domain",
            definition="The software we own. Used for Portfolio Management and Rationalization.",
            naming_convention="[Vendor] [Product Name] (e.g., 'Microsoft Teams')"
        )

    elif step == 'res_app_svc':
        show_result(
            table_name="Application Service",
            domain="Manage Technical Domain",
            definition="A deployed stack of the application. The operational entry point for Incident/Change.",
            naming_convention="[App Name] - [Environment] (e.g., 'Zoom - Prod')"
        )

    elif step == 'res_bus_svc':
        show_result(
            table_name="Business Service",
            domain="Consume Domain",
            definition="A service published to business users, usually via Request Catalog.",
            naming_convention="[Verb] [Noun] (e.g., 'Onboard Employee')"
        )

    elif step == 'res_tech_svc':
        show_result(
            table_name="Technical Service",
            domain="Manage Technical Domain",
            definition="A service provided by IT to IT. The technology grouping.",
            naming_convention="[Technology] Hosting/Support (e.g., 'Windows Hosting')"
        )

    elif step == 'res_tech_svc_off':
        show_result(
            table_name="Technical Service Offering",
            domain="Consume/Manage Domain",
            definition="A specific variant of the technical service with defined commitments (SLA).",
            naming_convention="[Service] - [Tier] (e.g., 'Windows Hosting - Gold')"
        )

    elif step == 'res_dyn_ci':
        show_result(
            table_name="Dynamic CI Group",
            domain="Foundation / Manage",
            definition="A group of CIs populated automatically by a CMDB Query.",
            naming_convention="[OS/Type] - [Location/Attribute] (e.g., 'Windows - NY')"
        )

    elif step == 'res_unknown':
        st.error("### Result: Unknown / Infrastructure CI")
        st.write("This item does not fit the standard CSDM Service/Application model.")
        st.info("It might be a standalone Server, Router, or Printer (Infrastructure CI). Check if this item should be discovered automatically via Discovery.")
        if st.button("🔄 Start Over", use_container_width=True):
            restart()

    # ---------------- FOOTER ----------------
    
    if st.session_state.history:
        st.markdown("---")
        if st.button("⬅️ Back to Previous Step"):
            go_back()
            st.rerun()

if __name__ == "__main__":
    main()