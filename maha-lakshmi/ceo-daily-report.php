<?php
// ========================================================================
// 🏢 MAHA LAKSHMI - CEO DAILY REPORT DASHBOARD
// GAURANGA - Digital Company Builder
// Owner: Prahlad
// Auto-Update: Setiap hari jam 6 AM WIB
// ========================================================================

session_start();

// Simple authentication
$valid_users = [
    'ceo' => 'MahaLakshmi2024',
    'gauranga' => 'AutoReport123'
];

$is_authenticated = false;
if (isset($_SESSION['logged_in']) && $_SESSION['logged_in'] === true) {
    $is_authenticated = true;
} elseif (isset($_POST['username']) && isset($_POST['password'])) {
    if (isset($valid_users[$_POST['username']]) && $valid_users[$_POST['username']] === $_POST['password']) {
        $_SESSION['logged_in'] = true;
        $_SESSION['username'] = $_POST['username'];
        $is_authenticated = true;
    }
}

if (isset($_GET['logout'])) {
    session_destroy();
    header('Location: ceo-daily-report.php');
    exit;
}

if (!$is_authenticated) {
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Maha Lakshmi CEO Report</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Nunito:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Nunito', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .login-container {
            background: white;
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 25px 70px rgba(0,0,0,0.3);
            max-width: 400px;
            width: 90%;
        }
        .login-container h1 {
            font-family: 'Playfair Display', serif;
            color: #1a5f5a;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2rem;
        }
        .login-container p {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
        }
        .form-group input {
            width: 100%;
            padding: 14px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        .form-group input:focus {
            outline: none;
            border-color: #1a5f5a;
        }
        .btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #1a5f5a, #2d8a84);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            transition: transform 0.3s;
        }
        .btn:hover {
            transform: translateY(-2px);
        }
        .error {
            background: #fee;
            color: #c00;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>👑 MAHA LAKSHMI</h1>
        <p>CEO Dashboard - Login Required</p>
        <?php if (isset($error)): ?>
            <div class="error"><?php echo $error; ?></div>
        <?php endif; ?>
        <form method="POST">
            <div class="form-group">
                <label>Username</label>
                <input type="text" name="username" required placeholder="Masukkan username">
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" name="password" required placeholder="Masukkan password">
            </div>
            <button type="submit" class="btn">Masuk</button>
        </form>
    </div>
</body>
</html>
<?php
    exit;
}

// ========================================================================
// DAILY REPORT DATA
// ========================================================================

$today = date('Y-m-d');
$yesterday = date('Y-m-d', strtotime('-1 day'));
$current_month = date('F Y');
$current_day = date('l, d F Y');

// 10 Companies Data
$companies = [
    1 => [
        'name' => 'Gianyar Tech Solutions',
        'short' => 'GTS',
        'niche' => 'Software Development & SaaS',
        'status' => 'active',
        'revenue' => 0,
        'target' => 10000000,
        'progress' => 0,
        'agents' => 4,
        'done' => [
            'Folder structure created',
            'Agent templates configured',
            'Company vision defined',
            'Initial market research'
        ],
        'doing' => [
            'Building first SaaS product',
            'Setting up development environment',
            'Creating MVP requirements'
        ],
        'next' => [
            'Deploy first product',
            'Generate first leads',
            'Setup payment gateway'
        ]
    ],
    2 => [
        'name' => 'Bali Digital Agency',
        'short' => 'BDA',
        'niche' => 'Web Development & Design',
        'status' => 'active',
        'revenue' => 0,
        'target' => 10000000,
        'progress' => 0,
        'agents' => 4,
        'done' => [
            'Portfolio website template ready',
            'Service packages defined',
            'Pricing strategy set',
            'Client acquisition funnel'
        ],
        'doing' => [
            'Building portfolio website',
            'Creating case studies',
            'Setting up inquiry form'
        ],
        'next' => [
            'Launch portfolio',
            'Start client outreach',
            'First project acquisition'
        ]
    ],
    3 => [
        'name' => 'Gianyar E-commerce',
        'short' => 'GEC',
        'niche' => 'Online Marketplace',
        'status' => 'planning',
        'revenue' => 0,
        'target' => 8000000,
        'progress' => 0,
        'agents' => 3,
        'done' => [
            'Business model defined',
            'Product categories planned',
            'Supplier partnerships research'
        ],
        'doing' => [
            'Platform selection',
            'Vendor onboarding process'
        ],
        'next' => [
            'Setup e-commerce platform',
            'First vendor recruitment',
            'Soft launch'
        ]
    ],
    4 => [
        'name' => 'Bali EdTech',
        'short' => 'BET',
        'niche' => 'Online Education Platform',
        'status' => 'planning',
        'revenue' => 0,
        'target' => 10000000,
        'progress' => 0,
        'agents' => 3,
        'done' => [
            'Course topics defined',
            'Target audience identified',
            'Platform comparison done'
        ],
        'doing' => [
            'Curriculum development',
            'Video content planning'
        ],
        'next' => [
            'Create first course',
            'Setup learning platform',
            'Beta launch to test group'
        ]
    ],
    5 => [
        'name' => 'Gianyar Finance',
        'short' => 'GFN',
        'niche' => 'Financial Services',
        'status' => 'planning',
        'revenue' => 0,
        'target' => 15000000,
        'progress' => 0,
        'agents' => 3,
        'done' => [
            'Service offerings defined',
            'Compliance requirements researched',
            'Target market identified'
        ],
        'doing' => [
            'Building financial calculator tools',
            'Creating informative content'
        ],
        'next' => [
            'Launch free tools',
            'Start consulting services',
            'Build trust with content'
        ]
    ],
    6 => [
        'name' => 'Bali Logistics',
        'short' => 'BLOG',
        'niche' => 'Delivery & Shipping Services',
        'status' => 'planning',
        'revenue' => 0,
        'target' => 8000000,
        'progress' => 0,
        'agents' => 3,
        'done' => [
            'Route planning for Gianyar area',
            'Partner courier research',
            'Pricing structure defined'
        ],
        'doing' => [
            'Building tracking system',
            'Partner onboarding'
        ],
        'next' => [
            'Soft launch in Gianyar',
            'First 10 business partners',
            'Expand to Ubud & Tampaksiring'
        ]
    ],
    7 => [
        'name' => 'Gianyar FoodTech',
        'short' => 'GFT',
        'niche' => 'Food Delivery & Restaurant Tech',
        'status' => 'planning',
        'revenue' => 0,
        'target' => 8000000,
        'progress' => 0,
        'agents' => 3,
        'done' => [
            'Restaurant partners list',
            'Delivery zone mapping',
            'Commission structure'
        ],
        'doing' => [
            'Building restaurant dashboard',
            'Creating menu integration'
        ],
        'next' => [
            'First 5 restaurant partners',
            'Beta launch',
            'Marketing to local community'
        ]
    ],
    8 => [
        'name' => 'Bali Travel',
        'short' => 'BTRAV',
        'niche' => 'Tourism & Travel Services',
        'status' => 'active',
        'revenue' => 0,
        'target' => 10000000,
        'progress' => 0,
        'agents' => 4,
        'done' => [
            'Tour packages created',
            'Partnership with local guides',
            'Booking system setup',
            'Website landing page'
        ],
        'doing' => [
            'Marketing to travel agents',
            'Creating tour itineraries'
        ],
        'next' => [
            'First bookings',
            'Google Business optimization',
            'Partnership with hotels'
        ]
    ],
    9 => [
        'name' => 'Gianyar Property',
        'short' => 'GPROP',
        'niche' => 'Real Estate Services',
        'status' => 'planning',
        'revenue' => 0,
        'target' => 10000000,
        'progress' => 0,
        'agents' => 3,
        'done' => [
            'Property listings database',
            'Agent network built',
            'Commission structure'
        ],
        'doing' => [
            'Property photography',
            'Virtual tour setup'
        ],
        'next' => [
            'First property listings',
            'Agent training',
            'Marketing campaign'
        ]
    ],
    10 => [
        'name' => 'Gianyar Consulting',
        'short' => 'GCONS',
        'niche' => 'Business & IT Consulting',
        'status' => 'active',
        'revenue' => 0,
        'target' => 12000000,
        'progress' => 0,
        'agents' => 4,
        'done' => [
            'Service packages defined',
            'Expert team identified',
            'Case studies prepared',
            'Initial client outreach'
        ],
        'doing' => [
            'Building consulting proposals',
            'Free webinar series'
        ],
        'next' => [
            'First paying client',
            'Testimonials collection',
            'Scale to 5 clients'
        ]
    ]
];

// Calculate totals
$total_revenue = 0;
$total_target = 0;
$total_agents = 0;
$active_companies = 0;
$planning_companies = 0;

foreach ($companies as $c) {
    $total_revenue += $c['revenue'];
    $total_target += $c['target'];
    $total_agents += $c['agents'];
    if ($c['status'] === 'active') $active_companies++;
    else $planning_companies++;
}

$profit_share = 0.60; // 60% to CEO
$ceo_share = $total_revenue * $profit_share;
$reinvestment = $total_revenue * 0.40;

?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👑 MAHA LAKSHMI - CEO Daily Report</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Nunito:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #1a5f5a;
            --primary-light: #2d8a84;
            --secondary: #c9a86c;
            --success: #22c55e;
            --warning: #f59e0b;
            --danger: #ef4444;
            --dark: #1a1a2e;
            --light: #f8fafc;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Nunito', sans-serif;
            background: var(--light);
            color: #333;
            line-height: 1.6;
        }
        
        .header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            margin-bottom: 5px;
        }
        
        .header .subtitle {
            opacity: 0.9;
            font-size: 1.1rem;
        }
        
        .header .date {
            margin-top: 15px;
            font-size: 0.9rem;
            opacity: 0.8;
        }
        
        .logout {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255,255,255,0.2);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.85rem;
        }
        
        .logout:hover { background: rgba(255,255,255,0.3); }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 30px;
        }
        
        /* Summary Cards */
        .summary-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .summary-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05);
            text-align: center;
        }
        
        .summary-card .icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary), var(--primary-light));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 15px;
            color: white;
            font-size: 1.5rem;
        }
        
        .summary-card .number {
            font-size: 2rem;
            font-weight: 700;
            color: var(--primary);
        }
        
        .summary-card .label {
            color: #666;
            font-size: 0.9rem;
        }
        
        /* Profit Card */
        .profit-section {
            background: linear-gradient(135deg, var(--secondary) 0%, #d4a96a 100%);
            padding: 30px;
            border-radius: 20px;
            color: white;
            margin-bottom: 40px;
        }
        
        .profit-section h2 {
            font-family: 'Playfair Display', serif;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .profit-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }
        
        .profit-item {
            background: rgba(255,255,255,0.2);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }
        
        .profit-item .label {
            font-size: 0.85rem;
            opacity: 0.9;
            margin-bottom: 5px;
        }
        
        .profit-item .amount {
            font-size: 1.5rem;
            font-weight: 700;
        }
        
        .profit-item .note {
            font-size: 0.75rem;
            opacity: 0.8;
            margin-top: 5px;
        }
        
        /* Company Cards */
        .section-title {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .company-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 25px;
        }
        
        .company-card {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        }
        
        .company-header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            color: white;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .company-header h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
        }
        
        .company-header .badge {
            background: rgba(255,255,255,0.2);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8rem;
        }
        
        .company-header .badge.active { background: var(--success); }
        .company-header .badge.planning { background: var(--warning); }
        
        .company-body {
            padding: 20px;
        }
        
        .company-meta {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
            font-size: 0.9rem;
            color: #666;
        }
        
        .company-meta i { color: var(--primary); margin-right: 5px; }
        
        .progress-bar {
            background: #e0e0e0;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 15px;
        }
        
        .progress-bar .fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--success));
            border-radius: 4px;
        }
        
        .progress-text {
            display: flex;
            justify-content: space-between;
            font-size: 0.85rem;
            color: #666;
            margin-bottom: 20px;
        }
        
        .task-list {
            margin-top: 15px;
        }
        
        .task-section {
            margin-bottom: 15px;
        }
        
        .task-section h4 {
            font-size: 0.85rem;
            color: var(--primary);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .task-list ul {
            list-style: none;
            font-size: 0.85rem;
        }
        
        .task-list li {
            padding: 5px 0;
            padding-left: 20px;
            position: relative;
            color: #555;
        }
        
        .task-list li::before {
            content: '•';
            position: absolute;
            left: 5px;
            color: var(--primary);
        }
        
        .task-list.done li::before { color: var(--success); content: '✓'; }
        .task-list.next li::before { color: var(--warning); content: '→'; }
        
        .revenue-mini {
            background: var(--light);
            padding: 15px;
            border-radius: 10px;
            margin-top: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .revenue-mini .label { font-size: 0.85rem; color: #666; }
        .revenue-mini .amount { font-size: 1.3rem; font-weight: 700; color: var(--success); }
        
        /* Auto Transfer Section */
        .auto-transfer {
            background: linear-gradient(135deg, #065f46 0%, #059669 100%);
            padding: 30px;
            border-radius: 20px;
            color: white;
            margin-top: 40px;
        }
        
        .auto-transfer h2 {
            font-family: 'Playfair Display', serif;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .transfer-info {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }
        
        .transfer-item {
            background: rgba(255,255,255,0.15);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }
        
        .transfer-item .label { font-size: 0.85rem; opacity: 0.9; }
        .transfer-item .value { font-size: 1.5rem; font-weight: 700; margin: 10px 0; }
        .transfer-item .detail { font-size: 0.8rem; opacity: 0.8; }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 40px;
            color: #666;
            font-size: 0.9rem;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .profit-grid, .company-grid, .transfer-info {
                grid-template-columns: 1fr;
            }
            .company-meta { flex-direction: column; gap: 5px; }
        }
    </style>
</head>
<body>
    <div class="header" style="position: relative;">
        <a href="?logout" class="logout">Logout</a>
        <h1>👑 MAHA LAKSHMI</h1>
        <p class="subtitle">CEO Daily Report - 10 Digital Companies</p>
        <p class="date">📅 <?php echo $current_day; ?> | 🕐 Update: 6:00 AM WIB</p>
    </div>
    
    <div class="container">
        <!-- Summary -->
        <div class="summary-grid">
            <div class="summary-card">
                <div class="icon"><i class="fas fa-building"></i></div>
                <div class="number">10</div>
                <div class="label">Total Companies</div>
            </div>
            <div class="summary-card">
                <div class="icon"><i class="fas fa-check-circle"></i></div>
                <div class="number"><?php echo $active_companies; ?></div>
                <div class="label">Active</div>
            </div>
            <div class="summary-card">
                <div class="icon"><i class="fas fa-clock"></i></div>
                <div class="number"><?php echo $planning_companies; ?></div>
                <div class="label">Planning</div>
            </div>
            <div class="summary-card">
                <div class="icon"><i class="fas fa-robot"></i></div>
                <div class="number"><?php echo $total_agents; ?></div>
                <div class="label">Active Agents</div>
            </div>
            <div class="summary-card">
                <div class="icon"><i class="fas fa-coins"></i></div>
                <div class="number">Rp <?php echo number_format($total_revenue); ?></div>
                <div class="label">Total Revenue</div>
            </div>
            <div class="summary-card">
                <div class="icon"><i class="fas fa-chart-line"></i></div>
                <div class="number">Rp <?php echo number_format($total_target); ?></div>
                <div class="label">Monthly Target</div>
            </div>
        </div>
        
        <!-- Profit Distribution -->
        <div class="profit-section">
            <h2>💰 Laporan Pendapatan & Profit Distribution</h2>
            <p style="margin-bottom: 20px; opacity: 0.9;"><?php echo $current_month; ?></p>
            <div class="profit-grid">
                <div class="profit-item">
                    <div class="label">Total Revenue</div>
                    <div class="amount">Rp <?php echo number_format($total_revenue); ?></div>
                </div>
                <div class="profit-item">
                    <div class="label">CEO Share (60%)</div>
                    <div class="amount">Rp <?php echo number_format($ceo_share); ?></div>
                    <div class="note">→ BCA 6485086645</div>
                </div>
                <div class="profit-item">
                    <div class="label">Reinvestment (40%)</div>
                    <div class="amount">Rp <?php echo number_format($reinvestment); ?></div>
                    <div class="note">→ Company operations</div>
                </div>
                <div class="profit-item">
                    <div class="label">Progress</div>
                    <div class="amount"><?php echo round(($total_revenue / $total_target) * 100, 1); ?>%</div>
                    <div class="note">of Rp <?php echo number_format($total_target); ?></div>
                </div>
            </div>
        </div>
        
        <!-- Company Progress -->
        <h2 class="section-title"><i class="fas fa-building"></i> Progress 10 Perusahaan Digital</h2>
        
        <div class="company-grid">
            <?php foreach ($companies as $num => $c): ?>
            <div class="company-card">
                <div class="company-header">
                    <div>
                        <h3><?php echo $num; ?>. <?php echo $c['name']; ?></h3>
                        <small><?php echo $c['niche']; ?></small>
                    </div>
                    <span class="badge <?php echo $c['status']; ?>">
                        <?php echo $c['status'] === 'active' ? 'Active' : 'Planning'; ?>
                    </span>
                </div>
                <div class="company-body">
                    <div class="company-meta">
                        <span><i class="fas fa-robot"></i> <?php echo $c['agents']; ?> Agents</span>
                        <span><i class="fas fa-coins"></i> Target: Rp <?php echo number_format($c['target']); ?></span>
                    </div>
                    
                    <div class="progress-bar">
                        <div class="fill" style="width: <?php echo $c['progress']; ?>%"></div>
                    </div>
                    <div class="progress-text">
                        <span>Progress</span>
                        <span><?php echo $c['progress']; ?>%</span>
                    </div>
                    
                    <div class="task-list done">
                        <div class="task-section">
                            <h4>✅ Yang Sudah Dikerjakan</h4>
                            <ul>
                                <?php foreach ($c['done'] as $task): ?>
                                <li><?php echo $task; ?></li>
                                <?php endforeach; ?>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="task-list doing">
                        <div class="task-section">
                            <h4>🔄 Sedang Dikerjakan</h4>
                            <ul>
                                <?php foreach ($c['doing'] as $task): ?>
                                <li><?php echo $task; ?></li>
                                <?php endforeach; ?>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="task-list next">
                        <div class="task-section">
                            <h4>📋 Akan Dikerjakan</h4>
                            <ul>
                                <?php foreach ($c['next'] as $task): ?>
                                <li><?php echo $task; ?></li>
                                <?php endforeach; ?>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="revenue-mini">
                        <span class="label">Revenue: Rp <?php echo number_format($c['revenue']); ?></span>
                        <span class="amount"><?php echo round(($c['revenue'] / $c['target']) * 100, 1); ?>%</span>
                    </div>
                </div>
            </div>
            <?php endforeach; ?>
        </div>
        
        <!-- Auto Transfer -->
        <div class="auto-transfer">
            <h2>🏦 Sistem Auto Transfer - Agent GAURANGA</h2>
            <div class="transfer-info">
                <div class="transfer-item">
                    <div class="label">Schedule</div>
                    <div class="value">SETIAP HARI</div>
                    <div class="detail">Jam 6:00 AM WIB</div>
                </div>
                <div class="transfer-item">
                    <div class="label">Rekening Tujuan</div>
                    <div class="value">BCA 6485086645</div>
                    <div class="detail">a/n Prahlad (CEO)</div>
                </div>
                <div class="transfer-item">
                    <div class="label">Share Pattern</div>
                    <div class="value">60% - 25% - 10% - 5%</div>
                    <div class="detail">CEO - Reinvest - Agent - Reserve</div>
                </div>
            </div>
            <p style="margin-top: 20px; opacity: 0.9; text-align: center;">
                <i class="fas fa-info-circle"></i> 
                Agent GAURANGA akan otomatis mengeksekusi transfer profit ke rekening CEO setelah revenue masuk.
                Setiap malam jam 11 PM, sistem akan menghitung profit harian dan Menjadwalkan transfer untuk jam 6 AM besok.
            </p>
        </div>
        
        <!-- CEO Actions -->
        <div style="background: white; padding: 30px; border-radius: 20px; margin-top: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <h2 style="font-family: 'Playfair Display', serif; color: var(--primary); margin-bottom: 20px;">
                <i class="fas fa-tasks"></i> Aksi CEO yang Dibutuhkan
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
                <div style="background: var(--light); padding: 15px; border-radius: 10px;">
                    <h4 style="color: var(--primary); margin-bottom: 5px;">🔥 Priority 1</h4>
                    <p style="font-size: 0.9rem;">Setup payment gateway untuk semua perusahaan</p>
                </div>
                <div style="background: var(--light); padding: 15px; border-radius: 10px;">
                    <h4 style="color: var(--primary); margin-bottom: 5px;">🔥 Priority 2</h4>
                    <p style="font-size: 0.9rem;">Verifikasi & aktifkan BCA account</p>
                </div>
                <div style="background: var(--light); padding: 15px; border-radius: 10px;">
                    <h4 style="color: var(--primary); margin-bottom: 5px;">🔥 Priority 3</h4>
                    <p style="font-size: 0.9rem;">Deploy Gianyar Tech Solutions MVP</p>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>👑 MAHA LAKSHMI - CEO Dashboard | Generated by Agent GAURANGA</p>
            <p>🕐 Last Updated: <?php echo date('Y-m-d H:i:s'); ?> WIB | Next Update: Tomorrow 6 AM</p>
            <p style="margin-top: 10px;">Motto: "Setiap kesalahan harus ada solusinya!"</p>
        </div>
    </div>
</body>
</html>
<?php
?>
