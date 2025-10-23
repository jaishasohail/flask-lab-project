// Dashboard JavaScript - Member 2 (Frontend Lead)

// State management
const state = {
    currentSection: 'overview',
    messages: [],
    users: [],
    stats: {
        totalMessages: 0,
        totalUsers: 3,
        systemStatus: 'Active',
        uptime: '99.9%'
    }
};

// Initialize dashboard on load
document.addEventListener('DOMContentLoaded', function() {
    console.log('Dashboard initializing...');
    
    // Setup navigation
    setupNavigation();
    
    // Load initial data
    loadDashboardData();
    
    // Setup event listeners
    setupEventListeners();
    
    // Initialize chart
    initializeChart();
    
    console.log('Dashboard ready!');
});

// Navigation Setup
function setupNavigation() {
    const sidebarLinks = document.querySelectorAll('.sidebar-menu a');
    
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links
            sidebarLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Get section to show
            const sectionId = this.getAttribute('href').substring(1);
            showSection(sectionId);
        });
    });
}

// Show specific section
function showSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('.dashboard-section');
    sections.forEach(section => {
        section.style.display = 'none';
    });
    
    // Show selected section
    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.style.display = 'block';
        state.currentSection = sectionId;
        
        // Load section-specific data
        loadSectionData(sectionId);
    }
}

// Load dashboard data
async function loadDashboardData() {
    try {
        // Check system health
        const healthResponse = await fetch('/health');
        const healthData = await healthResponse.json();
        
        if (healthData.status === 'OK') {
            updateStats();
        }
        
        // Load messages if endpoint exists
        loadMessages();
        
    } catch (error) {
        console.error('Error loading dashboard data:', error);
        showNotification('Error loading data', 'error');
    }
}

// Update statistics
function updateStats() {
    document.getElementById('total-messages').textContent = state.stats.totalMessages;
    document.getElementById('total-users').textContent = state.stats.totalUsers;
    document.getElementById('system-status').textContent = state.stats.systemStatus;
    document.getElementById('uptime').textContent = state.stats.uptime;
}

// Load messages (if API exists)
async function loadMessages() {
    try {
        // This assumes you've added a /api/messages endpoint
        const response = await fetch('/api/messages');
        
        if (response.ok) {
            const data = await response.json();
            state.messages = data.messages || [];
            state.stats.totalMessages = state.messages.length;
            updateStats();
            renderMessages();
        }
    } catch (error) {
        console.log('Messages endpoint not available yet');
    }
}

// Render messages table
function renderMessages() {
    const tbody = document.getElementById('messagesTableBody');
    
    if (state.messages.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="empty-state">No messages yet. Create one to get started!</td></tr>';
        return;
    }
    
    tbody.innerHTML = state.messages.map((msg, index) => `
        <tr>
            <td>${index + 1}</td>
            <td>${msg.name || 'Anonymous'}</td>
            <td>${msg.message || msg.processed?.message || 'No message'}</td>
            <td>${formatDate(msg.created_at || msg.timestamp)}</td>
            <td>
                <button class="btn btn-sm btn-secondary" onclick="viewMessage(${index})">View</button>
                <button class="btn btn-sm btn-danger" onclick="deleteMessage(${index})">Delete</button>
            </td>
        </tr>
    `).join('');
}

// Format date
function formatDate(dateString) {
    if (!dateString) return 'N/A';
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
}

// Load section-specific data
function loadSectionData(sectionId) {
    switch(sectionId) {
        case 'messages':
            loadMessages();
            break;
        case 'analytics':
            loadAnalytics();
            break;
        case 'users':
            loadUsers();
            break;
    }
}

// Load analytics
async function loadAnalytics() {
    // Calculate statistics from messages
    if (state.messages.length === 0) {
        document.getElementById('avg-length').textContent = '0 words';
        document.getElementById('total-words').textContent = '0';
        document.getElementById('longest-msg').textContent = 'N/A';
        return;
    }
    
    const messages = state.messages.map(m => m.message || m.processed?.message || '');
    const wordCounts = messages.map(m => m.split(' ').length);
    const totalWords = wordCounts.reduce((a, b) => a + b, 0);
    const avgWords = Math.round(totalWords / messages.length);
    const longest = messages.reduce((a, b) => a.length > b.length ? a : b);
    
    document.getElementById('avg-length').textContent = `${avgWords} words`;
    document.getElementById('total-words').textContent = totalWords;
    document.getElementById('longest-msg').textContent = longest.substring(0, 50) + '...';
}

// Load users
function loadUsers() {
    // Users are static for this demo
    console.log('Users loaded');
}

// Setup event listeners
function setupEventListeners() {
    // Search functionality
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            filterMessages(e.target.value);
        });
    }
    
    // New message form
    const messageForm = document.getElementById('newMessageForm');
    if (messageForm) {
        messageForm.addEventListener('submit', handleNewMessage);
    }
}

// Filter messages
function filterMessages(query) {
    const filtered = state.messages.filter(msg => {
        const name = (msg.name || '').toLowerCase();
        const message = (msg.message || msg.processed?.message || '').toLowerCase();
        const searchTerm = query.toLowerCase();
        return name.includes(searchTerm) || message.includes(searchTerm);
    });
    
    // Temporarily update state for rendering
    const originalMessages = state.messages;
    state.messages = filtered;
    renderMessages();
    state.messages = originalMessages;
}

// Handle new message
async function handleNewMessage(e) {
    e.preventDefault();
    
    const name = document.getElementById('msgName').value;
    const message = document.getElementById('msgContent').value;
    
    try {
        const response = await fetch('/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, message })
        });
        
        const result = await response.json();
        
        if (response.ok) {
            showNotification('Message created successfully!', 'success');
            closeModal('messageModal');
            
            // Add to local state
            state.messages.push(result.received_data || { name, message });
            state.stats.totalMessages = state.messages.length;
            updateStats();
            renderMessages();
            
            // Reset form
            document.getElementById('newMessageForm').reset();
        } else {
            showNotification(result.message || 'Error creating message', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showNotification('Network error', 'error');
    }
}

// View message
function viewMessage(index) {
    const msg = state.messages[index];
    alert(`Message Details:\n\nName: ${msg.name}\nMessage: ${msg.message || msg.processed?.message}\nDate: ${formatDate(msg.created_at || msg.timestamp)}`);
}

// Delete message
function deleteMessage(index) {
    if (confirm('Are you sure you want to delete this message?')) {
        state.messages.splice(index, 1);
        state.stats.totalMessages = state.messages.length;
        updateStats();
        renderMessages();
        showNotification('Message deleted', 'success');
    }
}

// Modal functions
function openNewMessageModal() {
    document.getElementById('messageModal').style.display = 'block';
}

function openNewUserModal() {
    showNotification('User management coming soon!', 'info');
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
}

// Show notification
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : '#667eea'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 3000;
        animation: slideIn 0.3s;
    `;
    
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Save settings
function saveSettings() {
    const appName = document.getElementById('appName').value;
    const apiEndpoint = document.getElementById('apiEndpoint').value;
    const theme = document.querySelector('input[name="theme"]:checked').value;
    const notifications = document.getElementById('notifications').checked;
    
    // Save to localStorage
    localStorage.setItem('dashboardSettings', JSON.stringify({
        appName,
        apiEndpoint,
        theme,
        notifications
    }));
    
    showNotification('Settings saved successfully!', 'success');
}

// Initialize Chart (simple version - can be enhanced with Chart.js)
function initializeChart() {
    const canvas = document.getElementById('activityChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    
    // Simple bar chart
    const data = [45, 67, 89, 56, 78, 92, 67];
    const labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    
    canvas.width = canvas.offsetWidth;
    canvas.height = 300;
    
    const barWidth = canvas.width / data.length;
    const maxValue = Math.max(...data);
    
    // Draw bars
    data.forEach((value, index) => {
        const barHeight = (value / maxValue) * (canvas.height - 40);
        const x = index * barWidth + 10;
        const y = canvas.height - barHeight - 20;
        
        // Create gradient
        const gradient = ctx.createLinearGradient(0, y, 0, canvas.height);
        gradient.addColorStop(0, '#667eea');
        gradient.addColorStop(1, '#764ba2');
        
        ctx.fillStyle = gradient;
        ctx.fillRect(x, y, barWidth - 20, barHeight);
        
        // Draw label
        ctx.fillStyle = '#666';
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(labels[index], x + (barWidth - 20) / 2, canvas.height - 5);
        
        // Draw value
        ctx.fillStyle = '#333';
        ctx.fillText(value, x + (barWidth - 20) / 2, y - 5);
    });
}

// Refresh data periodically
setInterval(() => {
    if (state.currentSection === 'overview') {
        loadDashboardData();
    }
}, 30000); // Refresh every 30 seconds

// Export for debugging
window.dashboardState = state;

console.log('Dashboard JavaScript loaded successfully!');
