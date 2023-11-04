import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class FlappyBirdGame extends JFrame implements KeyListener, ActionListener {
    private int birdY = 200;
    private int birdVelocity = 0;
    private int gravity = 2;
    private int score = 0;
    private boolean isGamePaused = true;
    private boolean isGameStarted = false;

    private Timer timer;
    private int delay = 10;

    private List<Rectangle> pipes;
    private int pipeWidth = 50;
    private int pipeHeight = 300;
    private int pipeGap = 200;
    private int pipeX = 800;
    private int pipeSpeed = 5;

    private JButton startButton;

    public FlappyBirdGame() {
        setTitle("Flappy Bird Game");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        addKeyListener(this);
        setFocusable(true);
        setFocusTraversalKeysEnabled(false);

        startButton = new JButton("Start Game");
        startButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                startGame();
            }
        });

        add(startButton, BorderLayout.SOUTH);

        pipes = new ArrayList<>();
        addPipe(800);

        timer = new Timer(delay, this);
    }

    public void addPipe(int x) {
        int gapPosition = new Random().nextInt(200) + 50;
        pipes.add(new Rectangle(x, 0, pipeWidth, gapPosition));
        pipes.add(new Rectangle(x, gapPosition + pipeGap, pipeWidth, 600 - gapPosition - pipeGap));
    }

    public void paint(Graphics g) {
        // Draw the background
        g.setColor(Color.cyan);
        g.fillRect(0, 0, 800, 600);

        if (isGameStarted) {
            // Draw the bird (a simple rectangle)
            g.setColor(Color.yellow);
            g.fillRect(100, birdY, 40, 40);

            // Draw pipes
            g.setColor(Color.green);
            for (Rectangle pipe : pipes) {
                g.fillRect(pipe.x, pipe.y, pipe.width, pipe.height);
            }

            // Check for collisions
            for (Rectangle pipe : pipes) {
                if (birdY + 40 > 600 || birdY < 0 || (birdY + 40 > pipe.y && birdY < pipe.y + pipe.height && pipe.x < 140 && pipe.x + pipe.width > 100)) {
                    gameOver();
                }
            }

            // Move pipes
            for (Rectangle pipe : pipes) {
                pipe.x -= pipeSpeed;
            }

            // Remove off-screen pipes
            pipes.removeIf(pipe -> pipe.x + pipe.width < 0);

            // Add new pipe
            if (pipes.get(pipes.size() - 1).x < 400) {
                addPipe(800);
                score++;
            }
        }

        // Draw the ground
        g.setColor(Color.orange);
        g.fillRect(0, 550, 800, 50);

        // Display the score
        g.setColor(Color.white);
        g.setFont(new Font("Arial", Font.PLAIN, 30));
        g.drawString("Score: " + score, 20, 30);

        if (isGamePaused) {
            // Show a "Game Over" message
            g.setFont(new Font("Arial", Font.BOLD, 60));
            g.drawString("Game Over", 280, 300);
        }

        g.dispose();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (!isGamePaused) {
            birdVelocity += gravity;
            birdY += birdVelocity;
            repaint();
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_SPACE) {
            if (!isGamePaused) {
                birdVelocity = -20; // Bird jumps
            } else if (isGameStarted) {
                restartGame();
            }
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
    }

    public void startGame() {
        isGameStarted = true;
        startButton.setVisible(false);
        timer.start();
    }

    public void restartGame() {
        birdY = 200;
        birdVelocity = 0;
        score = 0;
        isGamePaused = false;
        pipes.clear();
        addPipe(800);
    }

    public void gameOver() {
        isGamePaused = true;
        startButton.setVisible(true);
    }

    public static void main(String[] args) {
        FlappyBirdGame game = new FlappyBirdGame();
        game.setVisible(true);
    }
}
