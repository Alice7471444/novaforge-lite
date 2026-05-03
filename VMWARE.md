# NovaForge Lite - VMware Installation Guide
## 🖥️ How to Run NovaForge Lite in VMware

---

## 📋 Requirements

### VMware Products
- VMware Workstation (Windows/Linux)
- VMware Fusion (Mac)
- VMware Player (Free)

### Recommended Settings
| Setting | Minimum | Recommended |
|---------|---------|-------------|
| RAM | 2 GB | 4 GB |
| CPU | 1 core | 2 cores |
| Storage | 20 GB | 40 GB |
| Display | 1024x768 | 1920x1080 |

---

## 🚀 Installation Steps

### Step 1: Create Virtual Machine
1. Open VMware
2. Click **Create New Virtual Machine**
3. Select **Custom (advanced)**
4. Click **Next**

### Step 2: Select OS
1. Select **Linux**
2. Select **Other Linux 6.x or later kernel (64-bit)**
3. Click **Next**

### Step 3: Name VM
1. Name: `NovaForge Lite`
2. Click **Browse** to select location
3. Click **Next**

### Step 4: Processors
1. **Number of processors**: 2
2. **Number of cores per processor**: 1
3. Click **Next**

### Step 5: RAM
1. Select **4 GB** (or 2 GB minimum)
2. Click **Next**

### Step 6: Network
1. Select **NAT** (recommended)
2. Click **Next**

### Step 7: Disk
1. Select **SCSI** (recommended)
2. Click **Next**

### Step 8: Storage
1. **Maximum disk size**: 40 GB
2. Select **Split virtual disk into multiple files**
3. Click **Next**

### Step 9: Customize
1. Click **Customize Hardware**
2. Under **Display**:
   - Enable **Accelerate 3D graphics**
   - Set VRAM to **256 MB** (or higher)
3. Click **Close**
4. Click **Finish**

### Step 10: Install
1. Click **Edit virtual machine settings**
2. Go to **CD/DVD**
3. Select **Use ISO image file**
4. Browse to **NovaForge-Lite-v1.0.0-x86_64.iso**
5. Click **OK**
6. Click **Power on**

---

## ⚡ Optimizing VMware

### Recommended Settings

#### Processor
- 2 cores
- Enable virtualization (VT-x/AMD-V)

#### Memory
- 4 GB (2 GB minimum)
- Reserve all memory

#### Display
- 3D graphics: ON
- VRAM: 256 MB+
- Resolution: 1920x1080

#### Network
- NAT (easiest)
- or Bridge (for direct network access)

#### Sound
- Auto-detect
- or Disable if issues

---

## 🛠️ Troubleshooting

### No 3D Acceleration
1. Edit VM settings
2. Display → Enable 3D graphics
3. Restart VM

### Low Resolution
1. Install VMware Tools
2. Or: `xrandr -s 1920x1080`

### Mouse Not Working
1. Click inside VM
2. If still issues, install VMware Tools

### Network Not Working
1. Check VMware network adapter
2. Try NAT instead of Bridged
3. Restart VMware services

### Sound Issues
1. Disable sound in VM settings
2. Or install VMware Tools

### Slow Performance
1. Allocate more RAM
2. Enable 3D acceleration
3. Use SSD for storage

---

## 🔧 VMware Tools

### Why Install?
- Better graphics
- Better mouse integration
- Shared folders
- Copy/paste
- Better performance

### Installation
1. Click **VM → Install VMware Tools**
2. Mount CD:
   ```bash
   sudo mount /dev/cdrom /mnt
   ```
3. Extract:
   ```bash
   tar -xf /mnt/VMwareTools-*.tar.gz -C /tmp
   ```
4. Install:
   ```bash
   sudo /tmp/vmware-tools-distrib/install.pl
   ```
5. Restart

---

## 🎮 Gaming in VMware

### Performance Tips
1. Allocate 4+ GB RAM
2. Enable 3D acceleration
3. Use dedicated GPU if available
4. Set VM CPU to 2+ cores

### Games
- Older games work well
- Modern games: expect lower performance
- Use Steam, GameMode compatible

---

## 📞 Support

### Common Issues

| Issue | Solution |
|-------|----------|
| Black screen | Enable 3D graphics |
| No mouse | Install VMware Tools |
| No network | Try NAT, restart VM |
| Slow | More RAM, enable 3D |
| Sound off | Enable sound in settings |

---

<p align="center">
  <strong>Enjoy NovaForge Lite in VMware! 🚀</strong>
</p>