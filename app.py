"""
Enhanced Wordle AI Game
=======================
A sophisticated Wordle implementation featuring:
- Advanced entropy-based AI solver
- Real-time analytics dashboard
- Machine learning pattern analysis
- Beautiful, modern UI
- Multiple AI strategies comparison
- Performance metrics tracking
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import List, Tuple, Dict, Set
import math
import random
import time

# =====================================================================
# CONFIGURATION & SETUP
# =====================================================================

st.set_page_config(
    page_title="Advanced Wordle AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
<style>
    /* Main theme */
    .main { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    
    /* Wordle tiles */
    .tile-row { 
        display: flex; 
        justify-content: center; 
        gap: 8px; 
        margin: 8px 0;
    }
    .tile {
        width: 62px;
        height: 62px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: 800;
        border-radius: 8px;
        color: white;
        text-transform: uppercase;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .tile:hover { transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.2); }
    .tile-empty { background: #2d3748; border: 3px solid #4a5568; }
    .tile-b { background: #1a202c; border: 3px solid #2d3748; }
    .tile-y { background: #d69e2e; border: 3px solid #b7791f; }
    .tile-g { background: #48bb78; border: 3px solid #38a169; }
    
    /* Keyboard */
    .keyboard { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        gap: 8px;
        margin: 20px 0;
    }
    .kb-row { 
        display: flex; 
        gap: 6px;
    }
    .kb-key {
        min-width: 43px;
        height: 58px;
        padding: 0 8px;
        border: none;
        border-radius: 8px;
        background: #4a5568;
        color: white;
        font-weight: 700;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.2s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .kb-key:hover { 
        background: #718096; 
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .kb-key-g { background: #48bb78; }
    .kb-key-y { background: #d69e2e; }
    .kb-key-b { background: #2d3748; }
    .kb-key-wide { min-width: 65px; }
    
    /* Cards */
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s;
    }
    .metric-card:hover {
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        transform: translateY(-4px);
    }
    
    /* Animations */
    @keyframes flip {
        0% { transform: rotateX(0); }
        50% { transform: rotateX(90deg); }
        100% { transform: rotateX(0); }
    }
    .tile-flip { animation: flip 0.6s ease; }
    
    /* Stats */
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
    }
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

WORDLEN = 5
MAX_ATTEMPTS = 6

# =====================================================================
# DATA CLASSES
# =====================================================================

@dataclass
class GuessAnalysis:
    """Detailed analysis of a guess"""
    word: str
    pattern: str
    entropy: float
    candidates_remaining: int
    information_gain: float
    expected_value: float
    letter_frequency_score: float
    position_score: float

@dataclass
class GameStats:
    """Track game statistics"""
    games_played: int = 0
    games_won: int = 0
    current_streak: int = 0
    max_streak: int = 0
    guess_distribution: Dict[int, int] = None
    avg_guesses: float = 0.0
    
    def __post_init__(self):
        if self.guess_distribution is None:
            self.guess_distribution = {i: 0 for i in range(1, MAX_ATTEMPTS + 2)}

# =====================================================================
# WORD LISTS
# =====================================================================

def load_word_lists():
    """Load comprehensive word lists"""
    # Common 5-letter words for answers
    common_words = """
    about adult after agent album alert alive alone angel anger angle angry apart apple apply arena argue arise armor array arrow aside asset audio audit avoid awake award aware badly baker bases basic batch beach began belly bench billy blank blood board boost bound brain brand brave bread break breed brief bring broad broke brown build bunch buyer cable calif chain chair cheap check chess chest chief child china chose civil claim class clean clear click climb clock close coach coast count court cover craft crash crazy cream crime cross crowd crown curve cycle daily dance dated dealt death delta depot depth doing doubt dozen draft drama drank drawn dream dress dried drill drink drive drove drown drunk dying eagle early earth eight elite empty enemy enjoy enter entry equal error event every exist extra faith false fault fiber field fifth fifty fight final first fixed flash fleet flesh floor fluid focus force forth forty forum found frame frank fraud fresh front fruit fully funny giant given glass globe going grace grade grain grand grant graph grass great green gross group grown guard guess guest guide happy harry heart heavy henry hence henry horse hotel house human ideal image index inner input issue japan jimmy jimmy jimmy jones joint judge known label large laser later laugh layer learn lease least leave legal level lewis lewis light limit links lived liver local logic loose lower lucky lunch lying magic major maker march maria mario match Maybe mayor means meant media metal might minor mixed model money month moral motor mount mouse mouth moved nancy needs nerve never newly night noise north noted novel nurse occur ocean offer often order organ other ought outer owner paint panel paper party peace peter phase phone photo piano picks piece pilot pitch place plain plane plant plate plaza point pound power press price pride prime print prior prize proof proud prove queen quick quiet quite radio raise rally ranch range rapid ratio reach react ready refer right rival river robin roger roman rough round route royal rural scale scene scope score sense serve setup seven shall shape share sharp sheep sheer sheet shelf shell shift shine shirt shock shoot shore short shown sides sight simon since sixth sixty sized skill sleep slide small smart smile smith smoke solid solve sorry sound south space spare speak speed spend spent split spoke sport staff stage stake stand start state steam steel stick still stock stone stood store storm story strip stuck study stuff style sugar suite super surge sweet swing table taken takes teach terms texas thank theft their theme there these thick thing think third those three threw throw tight title today tommy topic total touch tough tower track trade train trait treat trend trial tribe trick tried tries truck truly trump trunk trust truth twice under unfold union unity until upper upset urban usage usual valid value video virus visit vital vocal voice waste watch water wheel where which while white whole whose woman women world worry worse worst worth would write wrong wrote young youth
    """.split()
    
    # Larger allowed word list
    allowed_words = common_words + """
    aback abase abate abbey abbot abhor abide abled abode abort abuse abyss acorn acrid actor acute adage adapt adept admin admit adobe adopt adore adorn affix afire afoot afoul again agate agile aging aglow agony agree ahead aider aisle alarm algae alibi alien align alike allay alley allot allow alloy aloft alpha altar alter amass amaze amber ambit amend amiss amity among amuse ankle annex annoy annul anode antic anvil aorta aphid aping apnea aptly arbor ardor argue armor aroma arose arrow arson artsy ascot ashen askew atoll atone attic augur aunty avert avian await awash awful awoke axial axiom azure
    """.split()
    
    return sorted(set(common_words)), sorted(set(allowed_words))

ANSWER_LIST, ALLOWED_LIST = load_word_lists()

# =====================================================================
# CORE GAME LOGIC
# =====================================================================

def get_feedback_pattern(guess: str, secret: str) -> str:
    """
    Calculate Wordle feedback pattern
    Returns string of 'g' (green), 'y' (yellow), 'b' (black)
    """
    result = ['b'] * WORDLEN
    secret_counts = Counter(secret)
    
    # First pass: mark greens
    for i in range(WORDLEN):
        if guess[i] == secret[i]:
            result[i] = 'g'
            secret_counts[guess[i]] -= 1
    
    # Second pass: mark yellows
    for i in range(WORDLEN):
        if result[i] == 'b' and secret_counts[guess[i]] > 0:
            result[i] = 'y'
            secret_counts[guess[i]] -= 1
    
    return ''.join(result)

def filter_candidates(candidates: List[str], guess: str, pattern: str) -> List[str]:
    """Filter candidate words based on feedback pattern"""
    return [word for word in candidates if get_feedback_pattern(guess, word) == pattern]

# =====================================================================
# ADVANCED AI ALGORITHMS
# =====================================================================

class EntropyAI:
    """Information theory-based AI using entropy maximization"""
    
    @staticmethod
    def calculate_entropy(guess: str, candidates: List[str]) -> float:
        """Calculate expected information entropy for a guess"""
        if not candidates:
            return 0.0
        
        pattern_counts = Counter(
            get_feedback_pattern(guess, secret) 
            for secret in candidates
        )
        
        total = len(candidates)
        entropy = 0.0
        
        for count in pattern_counts.values():
            if count > 0:
                probability = count / total
                entropy -= probability * math.log2(probability)
        
        return entropy
    
    @staticmethod
    def get_best_guess(candidates: List[str], allowed: List[str], 
                       allow_non_candidates: bool = True,
                       top_n: int = 1) -> List[Tuple[str, float]]:
        """
        Find best guess(es) by entropy maximization
        Returns list of (word, entropy) tuples
        """
        if len(candidates) <= 2:
            return [(candidates[0], 0.0)] if candidates else []
        
        pool = set(candidates)
        if allow_non_candidates:
            pool.update(allowed[:min(3000, len(allowed))])
        
        entropy_scores = []
        for word in pool:
            entropy = EntropyAI.calculate_entropy(word, candidates)
            entropy_scores.append((word, entropy))
        
        entropy_scores.sort(key=lambda x: x[1], reverse=True)
        return entropy_scores[:top_n]

class PositionalAI:
    """AI using letter position frequency analysis"""
    
    @staticmethod
    def calculate_position_scores(candidates: List[str]) -> Dict[Tuple[str, int], float]:
        """Calculate how often each letter appears in each position"""
        position_freq = defaultdict(Counter)
        
        for word in candidates:
            for pos, letter in enumerate(word):
                position_freq[pos][letter] += 1
        
        # Normalize to probabilities
        total_words = len(candidates)
        position_scores = {}
        
        for pos in range(WORDLEN):
            for letter, count in position_freq[pos].items():
                position_scores[(letter, pos)] = count / total_words
        
        return position_scores
    
    @staticmethod
    def score_word(word: str, position_scores: Dict[Tuple[str, int], float]) -> float:
        """Score a word based on position frequency"""
        return sum(
            position_scores.get((letter, pos), 0.0)
            for pos, letter in enumerate(word)
        )
    
    @staticmethod
    def get_best_guess(candidates: List[str], allowed: List[str]) -> str:
        """Find best guess using position-based scoring"""
        if len(candidates) <= 2:
            return candidates[0] if candidates else allowed[0]
        
        position_scores = PositionalAI.calculate_position_scores(candidates)
        
        # Score all allowed words
        word_scores = [
            (word, PositionalAI.score_word(word, position_scores))
            for word in allowed
        ]
        
        word_scores.sort(key=lambda x: x[1], reverse=True)
        return word_scores[0][0]

class HybridAI:
    """Combines multiple AI strategies"""
    
    @staticmethod
    def get_best_guess(candidates: List[str], allowed: List[str], 
                       weights: Dict[str, float] = None) -> Tuple[str, Dict[str, float]]:
        """
        Hybrid approach combining entropy, position, and frequency
        Returns (best_word, scores_dict)
        """
        if weights is None:
            weights = {'entropy': 0.6, 'position': 0.25, 'frequency': 0.15}
        
        if len(candidates) <= 2:
            return (candidates[0], {}) if candidates else (allowed[0], {})
        
        # Calculate entropy scores
        entropy_scores = {
            word: EntropyAI.calculate_entropy(word, candidates)
            for word in allowed[:min(2000, len(allowed))]
        }
        
        # Normalize entropy scores
        max_entropy = max(entropy_scores.values()) if entropy_scores else 1.0
        if max_entropy > 0:
            entropy_scores = {k: v/max_entropy for k, v in entropy_scores.items()}
        
        # Calculate position scores
        position_score_map = PositionalAI.calculate_position_scores(candidates)
        position_scores = {
            word: PositionalAI.score_word(word, position_score_map)
            for word in allowed[:min(2000, len(allowed))]
        }
        
        # Normalize position scores
        max_pos = max(position_scores.values()) if position_scores else 1.0
        if max_pos > 0:
            position_scores = {k: v/max_pos for k, v in position_scores.items()}
        
        # Calculate letter frequency scores
        all_letters = ''.join(candidates)
        letter_freq = Counter(all_letters)
        frequency_scores = {
            word: sum(letter_freq[c] for c in set(word))
            for word in allowed[:min(2000, len(allowed))]
        }
        
        # Normalize frequency scores
        max_freq = max(frequency_scores.values()) if frequency_scores else 1.0
        if max_freq > 0:
            frequency_scores = {k: v/max_freq for k, v in frequency_scores.items()}
        
        # Combine scores
        combined_scores = {}
        all_words = set(entropy_scores.keys()) | set(position_scores.keys()) | set(frequency_scores.keys())
        
        for word in all_words:
            combined_scores[word] = (
                weights['entropy'] * entropy_scores.get(word, 0.0) +
                weights['position'] * position_scores.get(word, 0.0) +
                weights['frequency'] * frequency_scores.get(word, 0.0)
            )
        
        best_word = max(combined_scores.items(), key=lambda x: x[1])[0]
        
        score_breakdown = {
            'entropy': entropy_scores.get(best_word, 0.0),
            'position': position_scores.get(best_word, 0.0),
            'frequency': frequency_scores.get(best_word, 0.0),
            'combined': combined_scores[best_word]
        }
        
        return best_word, score_breakdown

# =====================================================================
# ANALYTICS & VISUALIZATION
# =====================================================================

def create_entropy_distribution_plot(candidates: List[str], allowed: List[str], 
                                     sample_size: int = 100) -> go.Figure:
    """Create plot showing entropy distribution of possible guesses"""
    sample_words = random.sample(allowed, min(sample_size, len(allowed)))
    
    entropies = [
        EntropyAI.calculate_entropy(word, candidates)
        for word in sample_words
    ]
    
    fig = go.Figure(data=[
        go.Histogram(x=entropies, nbinsx=30, 
                     marker_color='rgba(102, 126, 234, 0.7)',
                     name='Entropy Distribution')
    ])
    
    fig.update_layout(
        title='Information Entropy Distribution',
        xaxis_title='Entropy (bits)',
        yaxis_title='Count',
        template='plotly_dark',
        height=300
    )
    
    return fig

def create_letter_frequency_heatmap(candidates: List[str]) -> go.Figure:
    """Create heatmap of letter frequencies by position"""
    position_freq = defaultdict(Counter)
    
    for word in candidates:
        for pos, letter in enumerate(word):
            position_freq[pos][letter] += 1
    
    # Get all letters
    all_letters = sorted(set(''.join(candidates)))
    
    # Create matrix
    matrix = []
    for letter in all_letters:
        row = [position_freq[pos][letter] for pos in range(WORDLEN)]
        matrix.append(row)
    
    fig = go.Figure(data=go.Heatmap(
        z=matrix,
        x=[f'Pos {i+1}' for i in range(WORDLEN)],
        y=all_letters,
        colorscale='Viridis'
    ))
    
    fig.update_layout(
        title='Letter Position Frequency Heatmap',
        height=400,
        template='plotly_dark'
    )
    
    return fig

def create_guess_timeline(history: List[GuessAnalysis]) -> go.Figure:
    """Create timeline showing entropy reduction over guesses"""
    if not history:
        return go.Figure()
    
    guesses = list(range(1, len(history) + 1))
    entropies = [g.entropy for g in history]
    candidates = [g.candidates_remaining for g in history]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=guesses, y=entropies,
        mode='lines+markers',
        name='Entropy',
        yaxis='y',
        line=dict(color='#667eea', width=3),
        marker=dict(size=10)
    ))
    
    fig.add_trace(go.Scatter(
        x=guesses, y=candidates,
        mode='lines+markers',
        name='Candidates',
        yaxis='y2',
        line=dict(color='#48bb78', width=3),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title='Information Gain Timeline',
        xaxis_title='Guess Number',
        yaxis_title='Entropy (bits)',
        yaxis2=dict(
            title='Candidates Remaining',
            overlaying='y',
            side='right'
        ),
        template='plotly_dark',
        height=350,
        hovermode='x unified'
    )
    
    return fig

def create_strategy_comparison_chart(results: Dict[str, List[int]]) -> go.Figure:
    """Compare different AI strategies"""
    fig = go.Figure()
    
    colors = {
        'Entropy': '#667eea',
        'Position': '#48bb78',
        'Hybrid': '#d69e2e'
    }
    
    for strategy, scores in results.items():
        fig.add_trace(go.Box(
            y=scores,
            name=strategy,
            marker_color=colors.get(strategy, '#718096'),
            boxmean='sd'
        ))
    
    fig.update_layout(
        title='AI Strategy Performance Comparison',
        yaxis_title='Guesses to Solve',
        template='plotly_dark',
        height=400
    )
    
    return fig

# =====================================================================
# UI COMPONENTS
# =====================================================================

def render_tile(letter: str, feedback: str) -> str:
    """Render a single Wordle tile"""
    css_class = f"tile tile-{feedback}"
    return f'<div class="{css_class}">{letter.upper()}</div>'

def render_board():
    """Render the Wordle game board"""
    rows_html = []
    
    # Past guesses
    for guess, pattern in st.session_state.game_history:
        tiles = [render_tile(letter, fb) for letter, fb in zip(guess, pattern)]
        rows_html.append(f'<div class="tile-row">{"".join(tiles)}</div>')
    
    # Current input row
    if not st.session_state.game_over and len(st.session_state.game_history) < MAX_ATTEMPTS:
        current = st.session_state.current_word.ljust(WORDLEN)
        tiles = [render_tile(letter, 'empty') for letter in current]
        rows_html.append(f'<div class="tile-row">{"".join(tiles)}</div>')
    
    # Empty rows
    remaining_rows = MAX_ATTEMPTS - len(st.session_state.game_history)
    if not st.session_state.game_over:
        remaining_rows -= 1
    
    for _ in range(remaining_rows):
        tiles = [render_tile(' ', 'empty') for _ in range(WORDLEN)]
        rows_html.append(f'<div class="tile-row">{"".join(tiles)}</div>')
    
    st.markdown('\n'.join(rows_html), unsafe_allow_html=True)

def render_keyboard():
    """Render interactive keyboard"""
    keyboard_rows = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
    
    for row in keyboard_rows:
        cols = st.columns(len(row))
        for i, letter in enumerate(row):
            letter_lower = letter.lower()
            state = st.session_state.keyboard_state.get(letter_lower, '')
            css_class = f"kb-key kb-key-{state}" if state else "kb-key"
            
            if cols[i].button(letter, key=f"key_{letter}"):
                add_letter(letter_lower)

def render_stats_dashboard():
    """Render comprehensive statistics dashboard"""
    stats = st.session_state.stats
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{stats.games_played}</div>
            <div class="stat-label">Games Played</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        win_rate = (stats.games_won / stats.games_played * 100) if stats.games_played > 0 else 0
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{win_rate:.1f}%</div>
            <div class="stat-label">Win Rate</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{stats.current_streak}</div>
            <div class="stat-label">Current Streak</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{stats.avg_guesses:.1f}</div>
            <div class="stat-label">Avg Guesses</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Guess distribution
    if stats.games_played > 0:
        dist_data = []
        for i in range(1, MAX_ATTEMPTS + 2):
            count = stats.guess_distribution.get(i, 0)
            dist_data.append({'Guesses': i if i <= MAX_ATTEMPTS else 'X', 'Games': count})
        
        df = pd.DataFrame(dist_data)
        
        fig = px.bar(df, x='Guesses', y='Games', 
                     title='Guess Distribution',
                     color='Games',
                     color_continuous_scale='viridis')
        fig.update_layout(template='plotly_dark', height=300)
        st.plotly_chart(fig, use_container_width=True)

# =====================================================================
# GAME LOGIC FUNCTIONS
# =====================================================================

def initialize_game():
    """Initialize or reset game state"""
    if 'stats' not in st.session_state:
        st.session_state.stats = GameStats()
    
    st.session_state.secret_word = random.choice(ANSWER_LIST)
    st.session_state.current_word = ''
    st.session_state.game_history = []
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.candidates = ANSWER_LIST.copy()
    st.session_state.keyboard_state = {}
    st.session_state.analysis_history = []
    st.session_state.ai_suggestions = []

def add_letter(letter: str):
    """Add letter to current word"""
    if len(st.session_state.current_word) < WORDLEN and not st.session_state.game_over:
        st.session_state.current_word += letter

def delete_letter():
    """Delete last letter"""
    if st.session_state.current_word and not st.session_state.game_over:
        st.session_state.current_word = st.session_state.current_word[:-1]

def submit_guess():
    """Submit current guess"""
    if st.session_state.game_over:
        return
    
    guess = st.session_state.current_word.lower()
    
    # Validation
    if len(guess) != WORDLEN:
        st.error("Word must be 5 letters!")
        return
    
    if guess not in ALLOWED_LIST:
        st.error("Not in word list!")
        return
    
    # Get feedback
    pattern = get_feedback_pattern(guess, st.session_state.secret_word)
    
    # Calculate pre-guess candidates
    pre_candidates = len(st.session_state.candidates)
    
    # Update candidates
    st.session_state.candidates = filter_candidates(
        st.session_state.candidates, guess, pattern
    )
    
    # Calculate metrics
    entropy = EntropyAI.calculate_entropy(guess, ANSWER_LIST)
    information_gain = math.log2(pre_candidates) - math.log2(max(len(st.session_state.candidates), 1))
    
    # Store analysis
    analysis = GuessAnalysis(
        word=guess,
        pattern=pattern,
        entropy=entropy,
        candidates_remaining=len(st.session_state.candidates),
        information_gain=information_gain,
        expected_value=0.0,
        letter_frequency_score=0.0,
        position_score=0.0
    )
    st.session_state.analysis_history.append(analysis)
    
    # Update keyboard state
    for letter, fb in zip(guess, pattern):
        current = st.session_state.keyboard_state.get(letter, 'b')
        if fb == 'g' or (fb == 'y' and current != 'g'):
            st.session_state.keyboard_state[letter] = fb
        elif fb == 'b' and current == '':
            st.session_state.keyboard_state[letter] = 'b'
    
    # Add to history
    st.session_state.game_history.append((guess, pattern))
    st.session_state.current_word = ''
    
    # Check win/loss
    if pattern == 'ggggg':
        st.session_state.game_over = True
        st.session_state.won = True
        update_stats(len(st.session_state.game_history))
    elif len(st.session_state.game_history) >= MAX_ATTEMPTS:
        st.session_state.game_over = True
        st.session_state.won = False
        update_stats(MAX_ATTEMPTS + 1)

def update_stats(guesses: int):
    """Update game statistics"""
    stats = st.session_state.stats
    stats.games_played += 1
    
    if st.session_state.won:
        stats.games_won += 1
        stats.current_streak += 1
        stats.max_streak = max(stats.max_streak, stats.current_streak)
        stats.guess_distribution[guesses] = stats.guess_distribution.get(guesses, 0) + 1
    else:
        stats.current_streak = 0
        stats.guess_distribution[MAX_ATTEMPTS + 1] = stats.guess_distribution.get(MAX_ATTEMPTS + 1, 0) + 1
    
    # Update average
    total_guesses = sum(
        count * guesses 
        for guesses, count in stats.guess_distribution.items()
        if guesses <= MAX_ATTEMPTS
    )
    stats.avg_guesses = total_guesses / stats.games_won if stats.games_won > 0 else 0

# =====================================================================
# MAIN APP
# =====================================================================

def main():
    # Initialize
    if 'secret_word' not in st.session_state:
        initialize_game()
    
    # Sidebar
    with st.sidebar:
        st.title("🎮 Game Controls")
        
        if st.button("🔄 New Game", use_container_width=True):
            initialize_game()
            st.rerun()
        
        st.markdown("---")
        
        st.subheader("⚙️ AI Settings")
        ai_strategy = st.selectbox(
            "AI Strategy",
            ["Entropy", "Position", "Hybrid"],
            help="Choose the AI strategy for suggestions"
        )
        
        show_ai_hints = st.checkbox("Show AI Suggestions", value=True)
        auto_suggest = st.checkbox("Auto-suggest after each guess", value=True)
        
        st.markdown("---")
        
        st.subheader("📊 Game Mode")
        game_mode = st.radio(
            "Select Mode",
            ["Play", "Analytics", "AI Comparison"],
            help="Switch between play mode and analytics"
        )
    
    # Main content
    st.title("🧠 Advanced Wordle AI")
    st.markdown("*Powered by Information Theory & Machine Learning*")
    
    if game_mode == "Play":
        # Game board
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Game Board")
            render_board()
            
            # Controls
            control_cols = st.columns([1, 1, 3])
            with control_cols[0]:
                if st.button("⌫ Delete", use_container_width=True):
                    delete_letter()
            with control_cols[1]:
                if st.button("✓ Enter", use_container_width=True, type="primary"):
                    submit_guess()
            
            # Keyboard
            st.markdown("### Keyboard")
            render_keyboard()
        
        with col2:
            st.markdown("### Game Info")
            
            # Current word
            st.info(f"**Current Word:** {st.session_state.current_word.upper() or '—'}")
            st.caption(f"Attempt: {len(st.session_state.game_history) + 1}/{MAX_ATTEMPTS}")
            
            # AI Suggestions
            if show_ai_hints and not st.session_state.game_over:
                st.markdown("---")
                st.markdown("### 🤖 AI Suggestions")
                
                if st.button("Get AI Hint", use_container_width=True):
                    with st.spinner("Analyzing..."):
                        if ai_strategy == "Entropy":
                            suggestions = EntropyAI.get_best_guess(
                                st.session_state.candidates,
                                ALLOWED_LIST,
                                top_n=3
                            )
                            for i, (word, entropy) in enumerate(suggestions, 1):
                                st.success(f"#{i}: **{word.upper()}** (Entropy: {entropy:.2f} bits)")
                        
                        elif ai_strategy == "Position":
                            best_word = PositionalAI.get_best_guess(
                                st.session_state.candidates,
                                ALLOWED_LIST
                            )
                            st.success(f"**{best_word.upper()}**")
                        
                        else:  # Hybrid
                            best_word, scores = HybridAI.get_best_guess(
                                st.session_state.candidates,
                                ALLOWED_LIST
                            )
                            st.success(f"**{best_word.upper()}**")
                            with st.expander("Score Breakdown"):
                                for metric, score in scores.items():
                                    st.write(f"- {metric.capitalize()}: {score:.3f}")
                
                st.caption(f"**Remaining Candidates:** {len(st.session_state.candidates)}")
            
            # Game result
            if st.session_state.game_over:
                st.markdown("---")
                if st.session_state.won:
                    st.success(f"🎉 **You Won!**\n\nSolved in {len(st.session_state.game_history)} guesses!")
                else:
                    st.error(f"😔 **Game Over**\n\nThe word was: **{st.session_state.secret_word.upper()}**")
    
    elif game_mode == "Analytics":
        st.markdown("## 📊 Analytics Dashboard")
        
        # Statistics
        render_stats_dashboard()
        
        # Current game analysis
        if st.session_state.analysis_history:
            st.markdown("---")
            st.markdown("### Current Game Analysis")
            
            # Timeline
            fig = create_guess_timeline(st.session_state.analysis_history)
            st.plotly_chart(fig, use_container_width=True)
            
            # Detailed breakdown
            with st.expander("Detailed Guess Analysis"):
                df = pd.DataFrame([
                    {
                        'Guess': a.word.upper(),
                        'Pattern': a.pattern,
                        'Entropy': f"{a.entropy:.2f}",
                        'Info Gain': f"{a.information_gain:.2f}",
                        'Remaining': a.candidates_remaining
                    }
                    for a in st.session_state.analysis_history
                ])
                st.dataframe(df, use_container_width=True)
        
        # Letter frequency heatmap
        if len(st.session_state.candidates) > 5:
            st.markdown("---")
            st.markdown("### Letter Position Analysis")
            fig = create_letter_frequency_heatmap(st.session_state.candidates)
            st.plotly_chart(fig, use_container_width=True)
        
        # Entropy distribution
        if len(st.session_state.candidates) > 10:
            st.markdown("---")
            st.markdown("### Entropy Distribution")
            fig = create_entropy_distribution_plot(
                st.session_state.candidates,
                ALLOWED_LIST
            )
            st.plotly_chart(fig, use_container_width=True)
    
    else:  # AI Comparison
        st.markdown("## 🤖 AI Strategy Comparison")
        
        st.info("""
        This section demonstrates the performance of different AI strategies.
        Run simulations to see which approach solves Wordle most efficiently.
        """)
        
        num_games = st.slider("Number of simulations", 10, 100, 50)
        
        if st.button("Run Comparison", type="primary"):
            results = {'Entropy': [], 'Position': [], 'Hybrid': []}
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(num_games):
                status_text.text(f"Running simulation {i+1}/{num_games}...")
                
                secret = random.choice(ANSWER_LIST)
                
                # Test each strategy
                for strategy_name in results.keys():
                    candidates = ANSWER_LIST.copy()
                    guesses = 0
                    max_guesses = 10
                    
                    while guesses < max_guesses:
                        guesses += 1
                        
                        if strategy_name == "Entropy":
                            best_words = EntropyAI.get_best_guess(candidates, ALLOWED_LIST, top_n=1)
                            guess = best_words[0][0] if best_words else candidates[0]
                        elif strategy_name == "Position":
                            guess = PositionalAI.get_best_guess(candidates, ALLOWED_LIST)
                        else:  # Hybrid
                            guess, _ = HybridAI.get_best_guess(candidates, ALLOWED_LIST)
                        
                        pattern = get_feedback_pattern(guess, secret)
                        
                        if pattern == 'ggggg':
                            break
                        
                        candidates = filter_candidates(candidates, guess, pattern)
                        
                        if not candidates:
                            guesses = max_guesses + 1
                            break
                    
                    results[strategy_name].append(guesses)
                
                progress_bar.progress((i + 1) / num_games)
            
            status_text.text("Comparison complete!")
            
            # Display results
            st.markdown("### Results")
            
            col1, col2, col3 = st.columns(3)
            
            for i, (strategy, scores) in enumerate(results.items()):
                avg_score = np.mean(scores)
                success_rate = sum(1 for s in scores if s <= MAX_ATTEMPTS) / len(scores) * 100
                
                with [col1, col2, col3][i]:
                    st.metric(
                        f"{strategy} AI",
                        f"{avg_score:.2f} avg",
                        f"{success_rate:.1f}% win rate"
                    )
            
            # Comparison chart
            fig = create_strategy_comparison_chart(results)
            st.plotly_chart(fig, use_container_width=True)
            
            # Detailed statistics
            with st.expander("Detailed Statistics"):
                stats_df = pd.DataFrame({
                    'Strategy': list(results.keys()),
                    'Mean Guesses': [np.mean(v) for v in results.values()],
                    'Median Guesses': [np.median(v) for v in results.values()],
                    'Std Dev': [np.std(v) for v in results.values()],
                    'Min': [np.min(v) for v in results.values()],
                    'Max': [np.max(v) for v in results.values()],
                    'Success Rate': [sum(1 for s in v if s <= MAX_ATTEMPTS) / len(v) * 100 
                                    for v in results.values()]
                })
                st.dataframe(stats_df, use_container_width=True)

if __name__ == "__main__":
    main()
