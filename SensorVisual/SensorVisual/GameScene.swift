//
//  GameScene.swift
//  SensorVisual
//
//  Created by Manik on 11/10/2018.
//  Copyright © 2018 Manik. All rights reserved.
//

import SpriteKit
import GameplayKit
import CoreMotion

class GameScene: SKScene {
    
    private var label : SKLabelNode?
    private var spinnyNode : SKShapeNode?
    var motionManager = CMMotionManager()
    
    override func didMove(to view: SKView) {
        
        // Get label node from scene and store it for use later
        motionManager.startAccelerometerUpdates()
        motionManager.AccelerometerUpdateInterval = 0.1
        motionManager.startAccelerometerUpdates(to: OperationQueue.main())
       
        }
        
        // Create shape node to use during mouse interaction
    
    
    override func update(_ currentTime: TimeInterval) {
        // Called before each frame is rendered
    }
}
    
    

    
    


