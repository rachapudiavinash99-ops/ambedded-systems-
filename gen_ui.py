import os

base_dir = r'D:\ambedded systems\frontend\templates'
os.makedirs(base_dir, exist_ok=True)

sidebar_html = '''
        <!-- Sidebar -->
        <div class="col-md-2 sidebar position-fixed">
            <h4 class="text-center mb-4 text-white mt-3">SmartDevice Lab</h4>
            <a href="/" class="{dash_active}">📊 Dashboard</a>
            <a href="/devices" class="{dev_active}">📱 Devices</a>
            <a href="/hardware" class="{hw_active}">🔬 Hardware Monitor</a>
            <a href="/tests" class="{test_active}">🧪 Tests & Tasks</a>
            <a href="/alerts" class="{alert_active}">⚠️ Alerts</a>
            <a href="/settings" class="{set_active}">⚙️ Settings</a>
        </div>
'''

head_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SmartDevice Embedded Systems Lab</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f4f6f9; }
        .card { margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-radius: 10px; }
        .sidebar { height: 100vh; background: #343a40; color: white; padding-top: 20px; z-index: 1000; width: 16.666667%; }
        .sidebar a { color: #adb5bd; text-decoration: none; padding: 10px 20px; display: block; font-size: 1.1rem; }
        .sidebar a:hover { color: white; background: #495057; }
        .sidebar a.active { color: white; background: #0d6efd; border-radius: 5px; margin: 0 10px; }
        .main-content { margin-left: 16.666667%; padding: 2rem; width: 83.333333%; }
    </style>
</head>
<body>
<div class="container-fluid p-0">
    <div class="row g-0">
'''

foot_html = '''
    </div>
</div>
</body>
</html>
'''

# 1. Update Dashboard
with open(os.path.join(base_dir, 'dashboard.html'), 'w', encoding='utf-8') as f:
    f.write(head_html)
    f.write(sidebar_html.format(dash_active='active', dev_active='', hw_active='', test_active='', alert_active='', set_active=''))
    f.write('''
        <div class="col-md-10 main-content">
            <h2>Dashboard</h2>
            <p class="text-muted">Welcome to the central command center.</p>
            <div class="card p-4 mt-4">
                <h5>Resource Utilization Overview</h5>
                <canvas id="telemetryChart" height="80"></canvas>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script>
            const ctx = document.getElementById('telemetryChart').getContext('2d');
            new Chart(ctx, { type: 'bar', data: { labels: ['CPU', 'RAM', 'Storage'], datasets: [{ label: 'Usage %', data: [45, 80, 60], backgroundColor: ['#0d6efd', '#dc3545', '#ffc107'] }] } });
        </script>
    ''' + foot_html)

# 2. Devices
with open(os.path.join(base_dir, 'devices.html'), 'w', encoding='utf-8') as f:
    f.write(head_html)
    f.write(sidebar_html.format(dash_active='', dev_active='active', hw_active='', test_active='', alert_active='', set_active=''))
    f.write('''
        <div class="col-md-10 main-content">
            <h2>Manage Devices</h2>
            <p class="text-muted">Manage your virtual embedded smartphone testing fleet.</p>
            <button class="btn btn-primary mb-3 mt-2">+ Add New Device</button>
            <table class="table table-striped bg-white rounded shadow-sm">
                <thead><tr><th>ID</th><th>Model</th><th>Status</th><th>Action</th></tr></thead>
                <tbody>
                    <tr><td>DEV-001</td><td>Virtual Pixel 7</td><td><span class="badge bg-success">Online</span></td><td><button class="btn btn-sm btn-outline-danger">Stop</button></td></tr>
                    <tr><td>DEV-002</td><td>Virtual Galaxy S23</td><td><span class="badge bg-secondary">Offline</span></td><td><button class="btn btn-sm btn-outline-success">Start</button></td></tr>
                </tbody>
            </table>
        </div>
    ''' + foot_html)

# 3. Hardware Monitor
with open(os.path.join(base_dir, 'hardware.html'), 'w', encoding='utf-8') as f:
    f.write(head_html)
    f.write(sidebar_html.format(dash_active='', dev_active='', hw_active='active', test_active='', alert_active='', set_active=''))
    f.write('''
        <div class="col-md-10 main-content">
            <h2>Live Hardware Monitor <span class="badge bg-success fs-6 align-middle ms-2">Streaming WebSocket</span></h2>
            <p class="text-muted">Viewing live telemetry from Virtual Pixel 7 (DEV-001)</p>
            <div class="row mt-4">
                <div class="col-md-3"><div class="card p-3 text-center border-primary"><h5>CPU</h5><h3 id="cpu-val" class="text-primary">0%</h3></div></div>
                <div class="col-md-3"><div class="card p-3 text-center border-danger"><h5>RAM</h5><h3 id="ram-val" class="text-danger">0%</h3></div></div>
                <div class="col-md-3"><div class="card p-3 text-center border-success"><h5>Battery</h5><h3 id="bat-val" class="text-success">0%</h3></div></div>
                <div class="col-md-3"><div class="card p-3 text-center border-warning"><h5>Temp</h5><h3 id="temp-val" class="text-warning">0°C</h3></div></div>
            </div>
            <div class="card p-4 mt-3">
                <h5>Sensor Matrix</h5>
                <div class="row text-center mt-3">
                    <div class="col-3"><h6 class="text-muted">Accel X</h6><p id="ax" class="fw-bold fs-5">0.00</p></div>
                    <div class="col-3"><h6 class="text-muted">Accel Y</h6><p id="ay" class="fw-bold fs-5">0.00</p></div>
                    <div class="col-3"><h6 class="text-muted">Accel Z</h6><p id="az" class="fw-bold fs-5">0.00</p></div>
                    <div class="col-3"><h6 class="text-muted">Gyro X</h6><p id="gx" class="fw-bold fs-5">0.00</p></div>
                </div>
            </div>
        </div>
        <script>
            const ws = new WebSocket(`ws://${window.location.host}/ws/telemetry`);
            ws.onmessage = function(event) {
                const data = JSON.parse(event.data);
                document.getElementById('cpu-val').innerText = data.cpu.toFixed(1) + '%';
                document.getElementById('ram-val').innerText = data.ram.toFixed(1) + '%';
                document.getElementById('bat-val').innerText = data.battery.toFixed(1) + '%';
                document.getElementById('temp-val').innerText = data.temp.toFixed(1) + '°C';
                
                document.getElementById('ax').innerText = data.sensors.accel_x.toFixed(3);
                document.getElementById('ay').innerText = data.sensors.accel_y.toFixed(3);
                document.getElementById('az').innerText = data.sensors.accel_z.toFixed(3);
                document.getElementById('gx').innerText = data.sensors.gyro_x.toFixed(3);
            };
        </script>
    ''' + foot_html)

# 4. Tests
with open(os.path.join(base_dir, 'tests.html'), 'w', encoding='utf-8') as f:
    f.write(head_html)
    f.write(sidebar_html.format(dash_active='', dev_active='', hw_active='', test_active='active', alert_active='', set_active=''))
    f.write('''
        <div class="col-md-10 main-content">
            <h2>Automated Hardware Tests</h2>
            <div class="card p-4 mt-4">
                <h5>Run Diagnostic Suite</h5>
                <p>Execute the embedded systems validation scripts on DEV-001.</p>
                <button class="btn btn-success w-25" onclick="alert('Test suite executed successfully! Passed: 14/14 checks')">Run Full Diagnostics</button>
            </div>
            
            <h4 class="mt-5">Tasks Queue</h4>
            <ul class="list-group">
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    Thermal Stress Test
                    <span class="badge bg-primary rounded-pill">Pending</span>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    Battery Drain Simulation
                    <span class="badge bg-success rounded-pill">Complete</span>
                </li>
            </ul>
        </div>
    ''' + foot_html)

# 5. Alerts
with open(os.path.join(base_dir, 'alerts.html'), 'w', encoding='utf-8') as f:
    f.write(head_html)
    f.write(sidebar_html.format(dash_active='', dev_active='', hw_active='', test_active='', alert_active='active', set_active=''))
    f.write('''
        <div class="col-md-10 main-content">
            <h2>System Alerts</h2>
            <div class="mt-4">
                <div class="alert alert-danger d-flex align-items-center" role="alert">
                    <div><strong>CRITICAL:</strong> Thermal limit exceeded on DEV-001 (90°C) recorded 2 mins ago.</div>
                </div>
                <div class="alert alert-warning d-flex align-items-center" role="alert">
                    <div><strong>WARNING:</strong> CPU Throttling active to prevent hardware failure.</div>
                </div>
                <div class="alert alert-info d-flex align-items-center" role="alert">
                    <div><strong>INFO:</strong> New OTA firmware update successfully pushed to DEV-002.</div>
                </div>
            </div>
        </div>
    ''' + foot_html)

# 6. Settings
with open(os.path.join(base_dir, 'settings.html'), 'w', encoding='utf-8') as f:
    f.write(head_html)
    f.write(sidebar_html.format(dash_active='', dev_active='', hw_active='', test_active='', alert_active='', set_active='active'))
    f.write('''
        <div class="col-md-10 main-content">
            <h2>Platform Settings</h2>
            <div class="card p-4 mt-4 w-50">
                <label class="form-label fw-bold">Telemetry Polling Rate (ms)</label>
                <input type="number" class="form-control mb-4" value="1000">
                
                <label class="form-label fw-bold">Theme Preference</label>
                <select class="form-select mb-4">
                    <option>Light Mode</option>
                    <option>Dark Mode</option>
                    <option>Auto (System)</option>
                </select>
                
                <label class="form-label fw-bold">Alert Threshold (°C)</label>
                <input type="number" class="form-control mb-4" value="85">

                <button class="btn btn-primary mt-2" onclick="alert('Configuration saved to database!')">Save Settings</button>
            </div>
        </div>
    ''' + foot_html)
