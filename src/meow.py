r"""

1. Window Configuration

python
Copy
self.setWindowFlags(Qt.FramelessWindowHint)
self.setAttribute(Qt.WA_TranslucentBackground)
self.setMinimumSize(800, 600)
2. Main Container Structure

python
Copy
main_widget = QWidget()
main_layout = QVBoxLayout(main_widget)
main_layout.setContentsMargins(0, 0, 0, 0)
main_layout.setSpacing(0)
self.setCentralWidget(main_widget)
3. Title Bar Implementation

python
Copy
title_bar = QWidget()
title_bar.setFixedHeight(40)
title_bar.setStyleSheet(f" ""
    background: {COLORS['title_bar']};
    border-top-left-radius: {BORDER_RADIUS}px;
    border-top-right-radius: {BORDER_RADIUS}px;
    border-bottom: 1px solid #404040;
"" ")

# Title label
title_label = QLabel("My Editor", alignment=Qt.AlignCenter)
title_label.setStyleSheet(f"color: {COLORS['text_primary']};")

# Window controls
controls = QWidget()
controls_layout = QHBoxLayout(controls)
controls_layout.setContentsMargins(0, 0, 12, 0)
controls_layout.setSpacing(8)

# Create control buttons with icons
for icon_name in ["close.svg", "maximize.svg", "minimize.svg"]:
    btn = QPushButton()
    btn.setIcon(QIcon(f"icons/{icon_name}"))
    btn.setFixedSize(20, 20)
    btn.setStyleSheet("border: none; background: transparent;")
    controls_layout.addWidget(btn)

# Layout structure
title_layout = QHBoxLayout(title_bar)
title_layout.addStretch()
title_layout.addWidget(title_label)
title_layout.addStretch()
title_layout.addWidget(controls)
4. Bottom Bar Implementation

python
Copy
bottom_bar = QWidget()
bottom_bar.setFixedHeight(30)
bottom_bar.setStyleSheet(f" ""
    background: {COLORS['bottom_bar']};
    border-bottom-left-radius: {BORDER_RADIUS}px;
    border-bottom-right-radius: {BORDER_RADIUS}px;
"" ")

filename_label = QLabel("filename.meow")
filename_label.setStyleSheet(f" ""
    color: {COLORS['text_primary']};
    padding-right: 20px;
    font: italic 10px;
" "")

bottom_layout = QHBoxLayout(bottom_bar)
bottom_layout.addStretch()
bottom_layout.addWidget(filename_label)
5. Assembly

python
Copy
main_layout.addWidget(title_bar)
# Add main content area here (will get remaining space)
main_layout.addStretch()
main_layout.addWidget(bottom_bar)
6. Window Dragging Logic

python
Copy
def mousePressEvent(self, event):
    self.old_pos = event.globalPosition().toPoint()

def mouseMoveEvent(self, event):
    delta = event.globalPosition().toPoint() - self.old_pos
    self.move(self.x() + delta.x(), self.y() + delta.y())
    self.old_pos = event.globalPosition().toPoint()
"""
