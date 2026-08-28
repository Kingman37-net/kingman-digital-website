#!/bin/bash
# Usage: ./make_placeholder.sh approach "Our Approach"
page=$1
title=$2
cat > $page.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>$title | Kingman Digital Cyber Network</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="$title - Kingman Digital Cyber Network">
<link rel="icon" href="images/logo-transparent.png">
<style>
$(cat extra.css)
/* Reuse basic styles from index.html – minimal version */
:root { --primary:#0b7fab; --accent:#00d1ff; --dark:#0a0f14; --light:#fff; --muted:#b9c6cf; --bg-gradient:linear-gradient(180deg,#060b10,#0a1118); --card-bg:rgba(255,255,255,0.04); --border:rgba(255,255,255,0.08); --nav-bg:#0a1118; --footer-bg:#05080c; }
* { margin:0; padding:0; box-sizing:border-box; font-family:"Segoe UI",system-ui,sans-serif; }
body { background:var(--bg-gradient); color:var(--light); line-height:1.7; }
nav { position:fixed; top:0; width:100%; background:var(--nav-bg); border-bottom:1px solid var(--border); z-index:999; padding:1rem; }
.nav-container { display:flex; justify-content:space-between; align-items:center; max-width:1200px; margin:auto; }
.nav-menu { display:flex; gap:30px; list-style:none; }
.nav-menu a { color:var(--light); text-decoration:none; font-weight:600; }
.logo img { height:40px; }
.hamburger { display:none; }
.bar { display:block; width:25px; height:3px; margin:5px auto; background:var(--light); }
.theme-toggle { background:none; border:none; font-size:1.5rem; cursor:pointer; margin-left:1rem; }
header { text-align:center; padding:140px 20px 80px; }
h1 { font-size:2.5rem; }
h1 span { color:var(--accent); }
section { max-width:1000px; margin:auto; padding:70px 20px; text-align:center; }
p { color:var(--muted); }
footer { background:var(--footer-bg); padding:50px 20px 30px; color:var(--muted); }
</style>
</head>
<body>
$(cat nav.html)
<header>
  <h1>$title <span>Coming Soon</span></h1>
  <p>This page is under construction. Please check back later.</p>
</header>
<section>
  <p>For any inquiries, please <a href="contact.html" style="color:var(--accent);">contact us</a>.</p>
</section>
$(cat footer.html)
<script>
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');
  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => navMenu.classList.toggle('active'));
  }
  const toggle = document.getElementById('theme-toggle');
  if (localStorage.getItem('theme') === 'light') {
    document.body.classList.add('light');
    toggle.textContent = '☀️';
  }
  toggle.addEventListener('click', () => {
    document.body.classList.toggle('light');
    const isLight = document.body.classList.contains('light');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    toggle.textContent = isLight ? '☀️' : '🌙';
  });
</script>
</body>
</html>
