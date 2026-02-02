import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(
    page_title="CubeSimple CSDM Assistant", 
    page_icon="🧊",
    layout="wide"
)

# --- STYLING (CSDM Colors) ---
st.markdown("""
<style>
    .design { border-left: 6px solid #00B5AD; background-color: #F0FBFC; padding: 15px; border-radius: 5px; }
    .manage { border-left: 6px solid #F2711C; background-color: #FEF6F1; padding: 15px; border-radius: 5px; }
    .consume { border-left: 6px solid #21BA45; background-color: #F0FDF4; padding: 15px; border-radius: 5px; }
    .foundation { border-left: 6px solid #767676; background-color: #F9F9F9; padding: 15px; border-radius: 5px; }
    .big-font { font-size: 18px !important; }
</style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
def init_state():
    if 'step' not in st.session_state: st.session_state.step = 'start'
    if 'history' not in st.session_state: st.session_state.history = []

def navigate(next_step):
    st.session_state.history.append(st.session_state.step)
    st.session_state.step = next_step
    st.rerun()

def go_back():
    if st.session_state.history:
        st.session_state.step = st.session_state.history.pop()
        st.rerun()

def restart():
    st.session_state.step = 'start'
    st.session_state.history = []
    st.rerun()

# --- CONTENT COMPONENTS ---
def show_confusion_buster():
    """Shows the cheat sheet at the top."""
    with st.expander("❓ Confusion Buster: Business App vs. App Service vs. Tech Service"):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("**Business Application** (Design)")
            st.markdown("The **Brand Name** or Product.")
            st.caption("e.g. 'Microsoft Excel', 'Zoom'")
            st.markdown("*Use for: Budgeting, Licensing*")
        with c2:
            st.warning("**Application Service** (Manage)")
            st.markdown("The **Running Instance**.")
            st.caption("e.g. 'Zoom - Prod', 'SAP - Dev'")
            st.markdown("*Use for: Incidents, Change Mgmt*")
        with c3:
            st.error("**Technical Service** (Manage)")
            st.markdown("The **IT Utility**.")
            st.caption("e.g. 'Windows Hosting', 'Storage'")
            st.markdown("*Use for: IT Support Groups*")

def show_question(title, prompt, yes_target, no_target, tips=None):
    st.subheader(title)
    st.markdown(f"### {prompt}")
    if tips: st.info(tips)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES ✅", use_container_width=True): navigate(yes_target)
    with col2:
        if st.button("NO ❌", use_container_width=True): navigate(no_target)

def show_result(title, domain, style_class, definition, example, naming):
    st.markdown(f"""
    <div class="{style_class}">
        <h2>🎯 Result: {title}</h2>
        <h4>Domain: {domain}</h4>
        <hr>
        <p class="big-font"><strong>📖 Definition:</strong> {definition}</p>
        <p><strong>✅ Example:</strong> {example}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.subheader("📝 Naming Standard")
    st.code(naming)
    
    st.divider()
    if st.button("🔄 Classify New Item", use_container_width=True): restart()

# --- MAIN APP ---
def main():
    init_state()
    
    col1, col2 = st.columns([1,5])
    with col1: st.title("🧊")
    with col2: 
        st.title("CSDM Classifier")
        st.caption("CubeSimple Decision Tool")
    
    show_confusion_buster()
    st.divider()
    
    step = st.session_state.step

    # --- LOGIC FLOW ---

    if step == 'start':
        show_question(
            "Step 1: Strategic Strategy",
            "Is this a high-level Business Ability (Strategy)?",
            "res_bus_cap", "q_container",
            tips="Does this exist without computers? (e.g. 'Recruiting' is an ability, 'Workday' is the tool)."
        )

    elif step == 'q_container':
        show_question(
            "Step 2: Container Check",
            "Is this just a Folder/Container to group things?",
            "res_svc_port", "q_software",
            tips="You cannot 'order' or 'fix' this directly. It just holds other items."
        )

    elif step == 'q_software':
        # THE CRITICAL SPLIT
        st.subheader("Step 3: Software Check")
        st.markdown("### Does this represent Software or an Application?")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Yes, it's Software 💻", use_container_width=True):
                navigate('split_software')
        with c2:
            if st.button("No, it's a Service/Action 🛠️", use_container_width=True):
                navigate('q_service_type')

    elif step == 'split_software':
        st.error("⚠️ STOP: This is where everyone gets confused.")
        st.markdown("### Which aspect of the software is it?")
        
        c1, c2 = st.columns(2)
        with c1:
            st.info("Option A: The Brand (Product)")
            st.markdown("- Used for **Budgets & Licenses**")
            st.markdown("- Represents ALL instances (Dev/Test/Prod)")
            st.markdown("- *Example: 'We bought Zoom'*")
            if st.button("It's the Brand (Business App)"): navigate('res_bus_app')
            
        with c2:
            st.warning("Option B: The Instance (Running)")
            st.markdown("- Used for **Incidents & Change**")
            st.markdown("- It is a specific environment (Prod vs Dev)")
            st.markdown("- *Example: 'Zoom Production is down'*")
            if st.button("It's the Instance (App Service)"): navigate('res_app_svc')

    elif step == 'q_service_type':
        st.subheader("Step 4: Who is the Customer?")
        
        c1, c2 = st.columns(2)
        with c1:
            st.success("The Business User (Employee)")
            st.caption("HR, Finance, Sales users")
            if st.button("Business User"): navigate('res_bus_svc')
        with c2:
            st.error("The IT Team (Technical)")
            st.caption("Server Admins, Network Engineers")
            if st.button("IT Team"): navigate('q_tech_offering')

    elif step == 'q_tech_offering':
        show_question(
            "Step 5: Service vs. Offering",
            "Is this a specific Tier/SLA (Gold/Silver)?",
            "res_tech_off", "res_tech_svc",
            tips="Offerings have specific prices or commitments (e.g. Gold = 99.9% Uptime)."
        )

    # --- RESULTS ---

    elif step == 'res_bus_cap':
        show_result("Business Capability", "Design", "design",
                   "Abstract Strategy. The 'What' we do.", "Recruiting Management", "[Function] Management")

    elif step == 'res_svc_port':
        show_result("Service Portfolio", "Consume", "consume",
                   "A logical container for reporting.", "HR Services", "[Topic] Services")

    elif step == 'res_bus_app':
        show_result("Business Application", "Design", "design",
                   "The Software Product/Brand. (Budgeting/Archiving)", "Microsoft Teams", "[Vendor] [Product]")

    elif step == 'res_app_svc':
        show_result("Application Service", "Manage Tech", "manage",
                   "The Running Instance. (Incidents/Monitoring)", "Teams - Prod - NA", "[App] - [Env]")

    elif step == 'res_bus_svc':
        show_result("Business Service", "Consume", "consume",
                   "Action for an End-User.", "Onboard Employee", "[Verb] [Noun]")

    elif step == 'res_tech_svc':
        show_result("Technical Service", "Manage Tech", "manage",
                   "IT Utility for other IT teams.", "Windows Hosting", "[Tech] Hosting")

    elif step == 'res_tech_off':
        show_result("Technical Service Offering", "Manage Tech", "manage",
                   "Specific SLA Tier of a Tech Service.", "Windows Hosting - Gold", "[Service] - [Tier]")

    # --- FOOTER ---
    if st.session_state.history:
        st.divider()
        if st.button("⬅️ Back"): go_back()

if __name__ == "__main__":
    main()
