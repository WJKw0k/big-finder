B
    KDna-$  �               @   s�  d dl Z d dlZd dlmZ d dlmZmZ dZddddd	d
gZddddddgZ	ee	� ee� dZ
dZe	�edd�e
� e�edd�e� dZdd� Zdd� Zdd� Zdd� Zdd� Zed k�r�yd dlZW n   ed!� d dlZY nX yd dlZW n   ed"� d dlZY nX yd dlZW n   ed#� d dlZY nX yd d$lmZmZmZmZ W n,   ed%� d d$lmZmZmZmZ Y nX eje j��  d&� yd d'lmZ W n    ed(� d d'lmZ Y nX e�  dS ))�    N)�sleep)�randint�shufflez�"It's called CSA Big Finder, not CSA Little Finder. If you don't remember who your little is,
you might have more serious issues at hand. Anyways, go troll your little(s) or something.u!   Ooof tails? Unlucky. ¯\_(:o)_/¯u,   Shouldn't have picked heads... ¯\_(0^0)_/¯z8You're really good at picking the wrong outcome, huh? :Pu   Maybe next time? ¯\_('V ')-zHow unlucky can you be? (>_<)z@Imagine losing to a silly program made by a bad cs student (._.)zTold you not to pick tails XDzShoulda gone with heads OwOz:I didn't know someone could be this bad at guessing (*o* )zLosing? Wouldn't be me... @<@z/I think my cat could do better than you (.O_0.)uC   You better hope Heads or Tails isn't in your Squid Game... (´;_;`)zJDon't go to Vegas - you'll lose all your money if you're this bad. (U._ U)z;You still haven't won yet? Maybe you should give up...  X.X�   �   z-\|/\c             C   s   t d� td|  � d S )Ng      �?�
)r   �print)�msg� r
   �big_finder.py�sl_print   s    r   c             C   s   t �d| g� d S )N�install)�pip�main)�packager
   r
   r   r   $   s    r   c               C   s    t jtjddd�ddgd� d S )NzCSA BIG FINDER!Zunivers)ZfontZyellowZbold)Zattrs)�	termcolorZcprint�pyfigletZfiglet_formatr
   r
   r
   r   �print_intro(   s    r   c                s  dd� �dd� � dd� }� d��d�d	�}�d
�� d
�d�}dddddiddigd�g}�fdd�t D �� fdd�t D � }�x8td�D �]*}td|td| ��dd� td� t|| d�}|d }tdd�}	g }
x�t|	�D ]�}x�|D ]�}td� |
�rtd d!�dk�r|
��  ntd d"�d"k�r,|
�d#� |
�rHd$�	|
�}t|d$d%� t|dd� ||	d" kr�|| |kr�td||  � |dk�r�t
�d �}n
t�d �}t|� P q�W q�W t�  q�W td&� td'� dd(d)dd*idd+igd�g}td� t|| d�d) }|d*k�rHtd,� t�d-�d$d%� td!� td.� td!� td/� td!� ntd0� td!� ddd1dd2idd3idd4igd�g}td� td�d5�dd� t|| d�d1 }td6� td!� td7� td!� td8� td!� td9d:�}	g }
�x.t|	�D �] }�x|D �]}td� |
�r*td d!�dk�r*|
��  ntd d"�d"k�rD|
�d#� |
�r`d$�	|
�}t|d$d%� t|dd� ||	d" k�r�|�d;�k�s�|� d;�k�r�td<� td� td=� td"� td>� td"� td?� |d@�}td� tdAd$d%� td9� t|� tdB� t�  �q�W �q�W t�  d S )CNc             S   s   t �| d�S )N�red)r   �colored)�animr
   r
   r   r   -   s    zflip_coin.<locals>.redc             S   s   t �| d�S )N�blue)r   r   )r   r
   r
   r   r   0   s    zflip_coin.<locals>.bluec             S   s   t �| d�S )N�green)r   r   )r   r
   r
   r   r   3   s    zflip_coin.<locals>.greenzIt's Tails!zIt's Heads!)�Heads�Tails�-)r   r   �listzHeads or Tails?Zflip�namer   r   )�type�messager   �choicesc                s   g | ]}� |��qS r
   r
   )�.0�char)r   r
   r   �
<listcomp>H   s    zflip_coin.<locals>.<listcomp>c                s   g | ]}� |��qS r
   r
   )r!   r"   )r   r
   r   r#   H   s    �   zNumber of Tries Left: �   T)�flushr   )�style�   �   g�������?r   �   r   � � )�endZPFFFFFFFFFFFFFTzB6 LOSSES IN A ROW??? 	 You must be the worst guesser in the world!zYour Reply?Zrigged_responsez"THIS IS RIGGED. LEMME SEE THE COINzI've got one more try.zHeh, you mean this thing?  z-
zDI can assure you that the coin is guaranteed to be potentially fair!zP And it's all virtual anyways... Good luck trying to prove that I'm CHEATING lolz�Well, considering the way the last 6 guesses have gone, I'm gonna take a wiiiiild guess and say that you're not winning this one either, bucko�lastz	Sideways.z	Sideways?zSIDEWAYS?!?!?!?!?!?!?!�1zHAHAHAHAHAHAHA *wheeze*zmToday just isn't you're day, is it? Why'd you pick sideways, anyways? Looks like someone's finally lost it...z#Anyways, let's just end it here. <3r   �   �|z....zIt's... sideways?z_well look at that. Guess I underestimated you after all.  Or maybe you're the one that cheated.z7You won, so I guess I have to tell you who your big is.z SOMEONE IN CSA!!!!!!!!!!!zyour big is: (drumroll please)zFGood for you! Now say hi to your big for me! You can thank me later :))�
coin_anims�ranger   �str�promptr   r   �pop�append�join�heads_picked_taunt�tails_picked_tauntr   �exit)r'   r   ZoppositeZriggedZinitial_coinsZanims�iZ
coin_guessZguessZm_spinsZspaces�x�frameZspacingZtauntZresponser.   Z	last_coinr	   r
   )r   r   r   �	flip_coin,   s�    $














*r?   c              C   s  t tjdtjdtjdtjdtjdtjdtjdi�} ddddd	idd
igd�g}t	�  t
d� t|| d�}|d d	kr�td� td� tt� t�  td� td� td� td� td� td� tdt�dd� d d t�dd� d � td� td� td� td� t| � d S ) Nz#cc5454z#673ab7 boldr,   z#f44336 boldr   zAre you a Big or a Little?Zpositionr   ZBigZLittle)r   r   r   r    r   )r'   zUh...z1I think you might might have the wrong program...zWelcome!z)So you want to find who your big is, huh?r(   zWELL IT WON'T BE THAT EASY!!!z>You just have to be me in a reeeeaaaaal easy game - coin toss!zHere's a magical coin -> it's ZREDr   z when it's headsz and ZBLUEr   z when it's tailsr   zMall you have to do is guess it correctly ONE out of SEVEN times? Easy, right?z1heh-heh - let's get rolling! (or is it flipping?))�style_from_dict�Token�	SeparatorZQuestionMarkZSelectedZPointerZInstructionZAnswerZQuestionr   r   r5   r   �big_exit_msgr;   r   r   r   r?   )r'   Z	questionsZintro_answersr
   r
   r   r   �   sD    *r   �__main__r   �coloramar   )r@   rA   r5   rB   �
PyInquirer)�strip)�pprintrH   ) �sysr   Ztimer   Zrandomr   r   rC   r9   r:   ZinflammatoryZinflammatory_two�insertr2   r   r   r   r?   r   �__name__r   rE   r   rF   r@   rA   r5   rB   Zinit�stdout�isattyrH   r
   r
   r
   r   �<module>   sj    3
