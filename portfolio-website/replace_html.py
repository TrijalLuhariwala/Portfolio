import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace ShopX
html = html.replace('''                            <div class="project-carousel" id="shopx-carousel">
                                <div class="carousel-track">
                                    <img src="images/shopx-1.png" alt="ShopX 1" class="carousel-slide">
                                    <img src="images/shopx-2.png" alt="ShopX 2" class="carousel-slide">
                                    <img src="images/shopx-3.png" alt="ShopX 3" class="carousel-slide">
                                    <img src="images/shopx-4.png" alt="ShopX 4" class="carousel-slide">
                                </div>
                                <button class="carousel-btn prev">&#10094;</button>
                                <button class="carousel-btn next">&#10095;</button>
                                <div class="carousel-nav">
                                    <button class="carousel-indicator current-slide"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                </div>
                            </div>''', '''                            <img src="images/shopx-1.png" alt="ShopX" class="project-img">''')

# Water
html = html.replace('''                            <div class="project-carousel" id="water-carousel">
                                <div class="carousel-track">
                                    <img src="images/water-1.png" alt="Water Quality 1" class="carousel-slide">
                                    <img src="images/water-2.png" alt="Water Quality 2" class="carousel-slide">
                                    <img src="images/water-3.png" alt="Water Quality 3" class="carousel-slide">
                                    <img src="images/water-4.png" alt="Water Quality 4" class="carousel-slide">
                                </div>
                                <button class="carousel-btn prev">&#10094;</button>
                                <button class="carousel-btn next">&#10095;</button>
                                <div class="carousel-nav">
                                    <button class="carousel-indicator current-slide"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                </div>
                            </div>''', '''                            <img src="images/water-1.png" alt="Indian Lakes Water Quality" class="project-img">''')

# Neuro
html = html.replace('''                            <div class="project-carousel" id="neuro-carousel">
                                <div class="carousel-track">
                                    <img src="images/neuro-1.png" alt="Neuro Vision 1" class="carousel-slide">
                                    <img src="images/neuro-2.png" alt="Neuro Vision 2" class="carousel-slide">
                                    <img src="images/neuro-3.png" alt="Neuro Vision 3" class="carousel-slide">
                                    <img src="images/neuro-4.png" alt="Neuro Vision 4" class="carousel-slide">
                                </div>
                                <button class="carousel-btn prev">&#10094;</button>
                                <button class="carousel-btn next">&#10095;</button>
                                <div class="carousel-nav">
                                    <button class="carousel-indicator current-slide"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                </div>
                            </div>''', '''                            <img src="images/neuro-1.png" alt="Neuro Vision" class="project-img">''')

# MNREGA
html = html.replace('''                            <div class="project-carousel" id="mnrega-carousel">
                                <div class="carousel-track">
                                    <img src="images/mnrega1.png" alt="MNREGA Cover" class="carousel-slide">
                                    <img src="images/mnrega2.png" alt="MNREGA Analysis" class="carousel-slide">
                                    <img src="images/mnrega3.png" alt="MNREGA Efficiency" class="carousel-slide">
                                    <img src="images/mnrega4.png" alt="MNREGA Work" class="carousel-slide">
                                </div>
                                <button class="carousel-btn prev">&#10094;</button>
                                <button class="carousel-btn next">&#10095;</button>
                                <div class="carousel-nav">
                                    <button class="carousel-indicator current-slide"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                </div>
                            </div>''', '''                            <img src="images/mnrega1.png" alt="MNREGA Performance Dashboard" class="project-img">''')

# Census
html = html.replace('''                            <div class="project-carousel" id="census-carousel">
                                <div class="carousel-track">
                                    <img src="images/census-1.png" alt="Census 2011 Data 1" class="carousel-slide">
                                    <img src="images/census-2.png" alt="Census 2011 Data 2" class="carousel-slide">
                                    <img src="images/census-3.png" alt="Census 2011 Data 3" class="carousel-slide">
                                    <img src="images/census-4.png" alt="Census 2011 Data 4" class="carousel-slide">
                                </div>
                                <button class="carousel-btn prev">&#10094;</button>
                                <button class="carousel-btn next">&#10095;</button>
                                <div class="carousel-nav">
                                    <button class="carousel-indicator current-slide"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                    <button class="carousel-indicator"></button>
                                </div>
                            </div>''', '''                            <img src="images/census-1.png" alt="Census 2011 Data Analysis" class="project-img">''')

# Replace buttons iteratively using parts
button_data = [
    "images/shopx-1.png,images/shopx-2.png,images/shopx-3.png,images/shopx-4.png",
    "images/water-1.png,images/water-2.png,images/water-3.png,images/water-4.png",
    "images/neuro-1.png,images/neuro-2.png,images/neuro-3.png,images/neuro-4.png",
    "images/mnrega1.png,images/mnrega2.png,images/mnrega3.png,images/mnrega4.png",
    "images/census-1.png,images/census-2.png,images/census-3.png,images/census-4.png"
]

target_button = \
'''                                    <button class="flip-btn front-flip"
                                        onclick="this.closest('.project-card').classList.add('flipped')">''' \
if '''                                    <button class="flip-btn front-flip"
                                        onclick="this.closest('.project-card').classList.add('flipped')">''' in html else \
'''                                    <button class="flip-btn front-flip" onclick="this.closest('.project-card').classList.add('flipped')">''' \
if '''                                    <button class="flip-btn front-flip" onclick="this.closest('.project-card').classList.add('flipped')">''' in html else \
'''<button class="flip-btn front-flip" onclick="this.closest('.project-card').classList.add('flipped')">'''

# Let's cleanly split and replace:
print("Found target_button?", target_button in html)
parts = html.split(target_button)
if len(parts) == 6:
    new_html = parts[0]
    for i in range(len(button_data)):
        gallery_btn = f\'\'\'                                    <button class="gallery-btn icon-link" data-images="{button_data[i]}" title="View Gallery">
                                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                                                <circle cx="8.5" cy="8.5" r="1.5"></circle>
                                                <polyline points="21 15 16 10 5 21"></polyline>
                                            </svg>
                                        </button>
{target_button}\'\'\'
        new_html += gallery_btn + parts[i+1]
    
    html = new_html
else:
    print(f"Warning: Expected 6 parts, got {len(parts)}. HTML might not have been fully converted.")


# Add the modal to the bottom just above <footer>
modal_html = '''
    <!-- Gallery Modal -->
    <div id="gallery-modal" class="modal-overlay">
        <div class="modal-content">
            <button id="close-modal" class="modal-close">&times;</button>
            <div class="modal-carousel project-carousel" style="height:100%; width:100%; border:none; background:transparent;">
                <div id="modal-track" class="carousel-track"></div>
                <button id="modal-prev" class="carousel-btn prev">&#10094;</button>
                <button id="modal-next" class="carousel-btn next">&#10095;</button>
                <div id="modal-nav" class="carousel-nav" style="bottom: -20px;"></div>
            </div>
        </div>
    </div>

    <footer>'''
html = html.replace('    <footer>', modal_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
