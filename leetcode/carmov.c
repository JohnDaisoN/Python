#include <SDL2/SDL.h>
#include <stdio.h>
#include <math.h>

// Function to draw a circle
void draw_circle(SDL_Renderer *renderer, int x, int y, int radius) {
    int diameter = (radius * 2);

    int x_c = radius - 1;
    int y_c = 0;
    int tx = 1;
    int ty = 1;
    int error = (tx - diameter);

    while (x_c >= y_c) {
        // Draw the circle points
        SDL_RenderDrawPoint(renderer, x + x_c, y - y_c);
        SDL_RenderDrawPoint(renderer, x + x_c, y + y_c);
        SDL_RenderDrawPoint(renderer, x - x_c, y - y_c);
        SDL_RenderDrawPoint(renderer, x - x_c, y + y_c);
        SDL_RenderDrawPoint(renderer, x + y_c, y - x_c);
        SDL_RenderDrawPoint(renderer, x + y_c, y + x_c);
        SDL_RenderDrawPoint(renderer, x - y_c, y - x_c);
        SDL_RenderDrawPoint(renderer, x - y_c, y + x_c);

        if (error <= 0) {
            ++y_c;
            error += ty;
            ty += 2;
        }

        if (error > 0) {
            --x_c;
            tx += 2;
            error += (tx - diameter);
        }
    }
}

// Function to draw moving car
void draw_moving_car(SDL_Renderer *renderer) {
    int i;

    for (i = 0; i <= 420; i += 10) {
        // Set color of car as red
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);

        // Draw the circle for left wheel of car
        draw_circle(renderer, 65 + i, 330, 15);

        // Draw the circle for right wheel of car
        draw_circle(renderer, 145 + i, 330, 15);

        SDL_RenderPresent(renderer);
        SDL_Delay(100);

        // Clear the renderer
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
    }
}

// Driver code
int main() {
    SDL_Window *window;
    SDL_Renderer *renderer;

    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        printf("Error initializing SDL: %s\n", SDL_GetError());
        return 1;
    }

    // Create a window and renderer
    window = SDL_CreateWindow("Moving Car", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 640, 480, SDL_WINDOW_SHOWN);
    if (window == NULL) {
        printf("Error creating window: %s\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == NULL) {
        printf("Error creating renderer: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // Draw the moving car
    draw_moving_car(renderer);

    // Cleanup and quit
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
